# preprocessing/lemmatization.py

import spacy

def lemmatize_text(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    return lemmatized_tokens
