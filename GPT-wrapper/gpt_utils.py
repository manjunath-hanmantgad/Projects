# Import the OpenAI library
import openai 

# Set your OpenAI API key here for authentication
openai.api_key = 'openai_api_key_here'

# Default prompt to be used for generating descriptions for images
#prompt = "Describe the content of the image below:"

def interaction_with_gpt(jpeg_images, prompt):
    '''Generate image descriptions using OpenAI's GPT model.
    
    Args:
        jpeg_images (list): List of paths to JPEG images for which descriptions need to be generated.
        prompt (str): Custom prompt text to be used in addition to the default prompt.
    
    Returns:
        list: List of generated descriptions corresponding to the input images.
    '''
    responses = []  # List to store generated descriptions for each image
    
    # Iterate through each image path provided in the input list
    for img_path in jpeg_images:
        with open(img_path, 'rb') as img_file:
            # Generate a description for the current image using OpenAI's GPT model
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,  # Combine default and custom prompts with image path
                max_tokens=128,  # Limit the response to 128 tokens for concise descriptions
                n=1,
                images=[img_file]  # Provide the image file for processing
            )
            
            # Extract and store the generated description for the current image
            responses.append(response.choices[0].text.strip())
    
    return responses  # Return the list of generated descriptions for input images
