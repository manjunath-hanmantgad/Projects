 # preprocessing/missing_data.py

def impute_missing_values(df, column, placeholder='unknown'):
    df[column] = df[column].fillna(placeholder)
    return df
