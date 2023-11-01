# Import required modules and libraries
from flask import Flask, request, render_template
from pdf_utils import extract_from_pdf, conversion_from_pdf_to_jpeg
from gpt_utils import interaction_with_gpt
from csv_utils import save_to_csv
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the upload folder and create it if it does not exist
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template when the user visits the home page

# Define the route for handling file upload and processing
@app.route('/upload', methods=['POST'])
def upload():
    # Check if the 'file' field is present in the uploaded request
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']  # Get the uploaded file object from the request

    # Check if no file is selected
    if file.filename == '':
        return "No selected file"

    if file:
        zip_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_files.zip')
        file.save(zip_path)  # Save the uploaded file as 'uploaded_files.zip'

        pdf_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'pdf_files')
        os.makedirs(pdf_folder, exist_ok=True)  # Create a directory to store extracted PDF files

        # Extract text from PDF files and save them as JPEG images
        extract_from_pdf(zip_path, pdf_folder)
        jpeg_images = conversion_from_pdf_to_jpeg(pdf_folder)

        prompt = request.form['prompt']  # Get user input prompt from the form

        # Interact with the GPT model using the extracted JPEG images and user prompt
        gpt_responses = interaction_with_gpt(jpeg_images, prompt)

        output_folder = os.path.join(app.config['UPLOAD_FOLDER'], 'output')
        os.makedirs(output_folder, exist_ok=True)  # Create a directory to store output CSV files

        # Save GPT responses and corresponding JPEG images to CSV files
        # Handle CSV file creation status and get success flag
        success = save_to_csv(jpeg_images, gpt_responses, output_folder)

        # Check if CSV files were successfully created and generate appropriate message
        if success:
            message = "Process completed successfully. CSV files created."
        else:
            message = "Failed to create CSV files. Please check the logs for details."

        return render_template('index.html', message=message)  # Render the index.html template with the generated message

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
