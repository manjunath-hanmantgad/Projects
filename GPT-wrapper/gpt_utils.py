import openai 

openai.api_key = 'openai_api_key_here'
prompt = "Describe the content of the image below:"

def interaction_with_gpt(jpeg_images, prompt):
    '''Provide jpeg images and prompt'''
    responses = []
    for img_path in jpeg_images:
        with open(img_path,'rb') as img_file:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt = f"{prompt} {img_path}",
                max_tokens = 128,
                n=1,
                images=[img_file]
            )
            responses.append(response.choices[0].text.strip())
    return responses