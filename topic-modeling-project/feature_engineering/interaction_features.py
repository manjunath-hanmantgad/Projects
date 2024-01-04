# feature_engineering/interaction_features.py

def create_interaction_features(df, sentiment_column):
    # Example: Assume 'sentiment' column is available in the dataset
    # df['sentiment_interaction'] = df['time_duration'] * df['sentiment']

    # Additional interaction features:
    df['time_sentiment_interaction'] = df['time_duration'] * df[sentiment_column]

    # You can add more interaction features based on your dataset

    return df
