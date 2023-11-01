# Import necessary libraries and modules
import os 
import zipfile
from PyPDF2 import PdfFileReader
from PIL import Image

def extract_from_pdf(zip_file_path, output_folder):
    ''' Extract PDF files from a given zip file and save them to the specified output folder.
    
    Args:
        zip_file_path (str): Path to the input ZIP file containing PDFs.
        output_folder (str): Path to the folder where extracted PDF files will be saved.
    '''
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)  # Extract PDF files from the ZIP to the output folder

def conversion_from_pdf_to_jpeg(extracted_pdf_folder):
    ''' Convert PDF pages to JPEG images and return a list of image file paths.
    
    Args:
        extracted_pdf_folder (str): Path to the folder containing extracted PDF files.
    
    Returns:
        list: List of file paths for the converted JPEG images.
    '''
    jpeg_images = []  # List to store paths of converted JPEG images
    
    # Traverse through the extracted PDF folder and convert each page to JPEG
    for root, dirs, files in os.walk(extracted_pdf_folder):
        for file in files:
            if file.endswith('.pdf'):  # Check if the file is a PDF
                pdf_path = os.path.join(root, file)  # Get the full path to the PDF file
                with open(pdf_path, 'rb') as pdf_file:
                    pdf_reader = PdfFileReader(pdf_file)  # Create a PDF reader object
                    for page_num in range(pdf_reader.numPages):
                        page = pdf_reader.getPage(page_num)  # Get the current page
                        img = Image.open(page)  # Open the page as an image
                        img_path = os.path.join(root, f'page_{page_num + 1}.jpeg')  # Path for saving the JPEG image
                        img.save(img_path, 'JPEG')  # Save the image as JPEG format
                        jpeg_images.append(img_path)  # Add the image path to the list
                        
    return jpeg_images  # Return the list of converted JPEG image paths
