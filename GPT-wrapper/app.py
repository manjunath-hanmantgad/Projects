from flask import Flask, request, render_template
from pdf_utils import extract_from_pdf, conversion_from_pdf_to_jpeg
from gpt_utils import interaction_with_gpt
from csv_utils import save_to_csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_files.zip')
        file.save(zip_path)
        pdf_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'pdf_files')
        os.makedirs(pdf_folder, exist_ok=True)
        extract_from_pdf(zip_path, pdf_folder)
        jpeg_images = conversion_from_pdf_to_jpeg(pdf_folder)
        prompt = request.form['prompt']
        gpt_responses = interaction_with_gpt(jpeg_images, prompt)
        output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
        os.makedirs(output_folder, exist_ok=True)
        save_to_csv(jpeg_images, gpt_responses, output_folder)
        # Handle CSV file creation status
        success = save_to_csv(jpeg_images, gpt_responses, output_folder)
        if success:
            message = "Process completed successfully. CSV files created."
        else:
            message = "Failed to create CSV files. Please check the logs for details."
        
        return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
