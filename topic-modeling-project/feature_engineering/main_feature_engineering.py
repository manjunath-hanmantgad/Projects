# feature_engineering/main_feature_engineering.py

import pandas as pd
from preprocessing.text_preprocessing import preprocess_text
from feature_engineering.categorical_features import encode_categorical_features
from feature_engineering.datetime_features import create_datetime_features
from feature_engineering.domain_specific_features import engineer_domain_specific_features
from feature_engineering.handling_rare_categories import handle_rare_categories
from feature_engineering.numerical_features import create_numerical_features
from feature_engineering.interaction_features import create_interaction_features

# Load your dataset (replace 'your_dataset.csv' with the actual file name)
df = pd.read_csv('data/processed/your_dataset.csv')

# Assuming these are your categorical columns
categorical_columns = ['type_of_service', 'priority_level', 'channel_of_submission']

# Perform Text Preprocessing for all text columns
text_columns = ['short description', 'long description', 'closure notes','resolution', 'issue description']
for column in text_columns:
    df = preprocess_text(df, text_column=column)

# Encode Categorical Features
df = encode_categorical_features(df, columns_to_encode=categorical_columns)

# Additional Feature Engineering Steps
df = create_datetime_features(df, date_column='ticket solved date')  # Example: 'ticket solved date' as the date column
df = engineer_domain_specific_features(df)  # Example: Engineer domain-specific features
df = handle_rare_categories(df, categorical_columns=categorical_columns, threshold=0.05)  # Example: Handling rare categories
df = create_numerical_features(df)  # Example: Create numerical features
df = create_interaction_features(df, sentiment_column='sentiment_score')  # Example: Interaction features

# Continue with other feature engineering steps...

# Save the fully processed DataFrame
df.to_csv('data/processed/your_fully_processed_dataset.csv', index=False)
