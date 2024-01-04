# preprocessing/text_preprocessing.py

import pandas as pd
from text_cleaning import clean_text
from tokenization import tokenize_text
from lemmatization import lemmatize_text
from missing_data import impute_missing_values

def preprocess_text_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Apply text cleaning
    df['cleaned_short_description'] = df['short description'].apply(clean_text)
    df['cleaned_long_description'] = df['long description'].apply(clean_text)

    # Tokenization
    df['tokenized_short_description'] = df['cleaned_short_description'].apply(tokenize_text)
    df['tokenized_long_description'] = df['cleaned_long_description'].apply(tokenize_text)

    # Lemmatization
    df['lemmatized_short_description'] = df['cleaned_short_description'].apply(lemmatize_text)
    df['lemmatized_long_description'] = df['cleaned_long_description'].apply(lemmatize_text)

    # Handling missing data
    columns_to_impute = ['lemmatized_short_description', 'lemmatized_long_description']
    for column in columns_to_impute:
        df = impute_missing_values(df, column)

    
    # Save the processed data to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "data/data.csv"
    output_file = "data/processed_data.csv"

    preprocess_text_data(input_file, output_file)
