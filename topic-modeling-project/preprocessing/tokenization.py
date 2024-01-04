# preprocessing/tokenization.py

import spacy

def tokenize_text(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    tokens = [token.text for token in doc]
    return tokens
