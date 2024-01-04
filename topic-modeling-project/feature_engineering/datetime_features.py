# feature_engineering/datetime_features.py

import pandas as pd

def extract_datetime_features(df):
    df['ticket_opened_date'] = pd.to_datetime(df['ticket opened date'])
    df['ticket_solved_date'] = pd.to_datetime(df['ticket solved date'])

    df['day_of_week'] = df['ticket_opened_date'].dt.dayofweek
    df['month'] = df['ticket_opened_date'].dt.month
    df['time_of_day'] = df['ticket_opened_date'].dt.hour

    df['year'] = df['ticket_opened_date'].dt.year
    df['quarter'] = df['ticket_opened_date'].dt.quarter
    df['weekday_indicator'] = (df['ticket_opened_date'].dt.weekday < 5).astype(int)

    return df
