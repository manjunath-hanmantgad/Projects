import csv 
import os

def save_to_csv(jpeg_images,gpt_responses,output_folder):
    ''''''
    try:
        
        for i,img_path in enumerate(jpeg_images):
            csv_path = os.path.join(output_folder, f'output_{i+1}.csv')
            with open(csv_path,'w',newline='',encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Image Path','GPT Response'])
                csv_writer.writerow([img_path,gpt_responses[i]])
        return True 
    except Exception as e:
        print(f"Error: {e}")
        return False