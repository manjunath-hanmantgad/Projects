# Import required libraries
import csv 
import os

def save_to_csv(jpeg_images, gpt_responses, output_folder):
    '''Save image paths and corresponding GPT responses to CSV files.

    Args:
        jpeg_images (list): List of paths to JPEG images.
        gpt_responses (list): List of GPT responses corresponding to the input images.
        output_folder (str): Path to the folder where CSV files will be saved.

    Returns:
        bool: True if the CSV files are successfully created, False otherwise.
    '''
    try:
        # Iterate through the provided image paths and corresponding GPT responses
        for i, img_path in enumerate(jpeg_images):
            # Create the path for the CSV file using the output folder and index
            csv_path = os.path.join(output_folder, f'output_{i + 1}.csv')
            
            # Open the CSV file in write mode with UTF-8 encoding
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)  # Create a CSV writer object
                
                # Write the header row containing column names: 'Image Path' and 'GPT Response'
                csv_writer.writerow(['Image Path', 'GPT Response'])
                
                # Write a row with the current image path and corresponding GPT response
                csv_writer.writerow([img_path, gpt_responses[i]])
        
        return True  # Return True indicating successful CSV file creation
    
    except Exception as e:
        print(f"Error: {e}")  # Print the error message if an exception occurs
        return False  # Return False indicating failure in CSV file creation
