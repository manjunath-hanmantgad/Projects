# feature_engineering/numerical_features.py

def extract_numerical_features(df):
    df['time_duration'] = (df['ticket_solved_date'] - df['ticket_opened_date']).dt.total_seconds()
    return df
