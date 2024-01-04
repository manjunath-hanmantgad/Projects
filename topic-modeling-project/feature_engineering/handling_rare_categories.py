# feature_engineering/handling_rare_categories.py

def handle_rare_categories(df, categorical_columns, threshold=0.05):
    for column in categorical_columns:
        counts = df[column].value_counts(normalize=True)
        rare_categories = counts[counts < threshold].index
        df[column] = df[column].replace(rare_categories, 'Other')
    return df
