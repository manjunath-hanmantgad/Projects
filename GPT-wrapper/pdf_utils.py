#imports

import os 
import zipfile
from PyPDF2 import PdfFileReader #it installs as pypdf2
from PIL import Image

def extract_from_pdf(zip_file_path,output_folder):
    ''' input is path to zip file and folder containing the
        output. 
        Function: extract pdf files from zip and save them
        to given output folder.'''
    with zipfile.ZipFile(zip_file_path,'r') as zip_ref:
        zip_ref.extractall(output_folder)
        
def conversion_from_pdf_to_jpeg(extracted_pdf_folder):
    '''input is folder containing pdf files.
        Convert each page in pdf to jpeg images
        and returns list of paths of images.'''
    jpeg_images = []
    for root,dirs,files in os.walk(extracted_pdf_folder):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root,file)
                with open(pdf_path,'rb') as pdf_file:
                    pdf_reader = PdfFileReader(pdf_file)
                    for page_num in range(pdf_reader.numPages):
                        page = pdf_reader.getPage(page_num)
                        img = Image.open(page)
                        img_path = os.path.join(root, f'page_{page_num + 1}.jpeg')
                        img.save(img_path, 'JPEG')
                        jpeg_images.append(img_path)
    return jpeg_images

