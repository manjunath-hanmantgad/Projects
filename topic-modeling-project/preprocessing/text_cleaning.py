# preprocessing/text_cleaning.py

import re
from bs4 import BeautifulSoup

def clean_text(text):
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Handle HTML tags or markup
    text = BeautifulSoup(text, 'html.parser').get_text()
    
    return text
