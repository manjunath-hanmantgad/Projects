# feature_engineering/domain_specific_features.py

def engineer_domain_specific_features(df):
    # Example: Assume 'network_type', 'customer_tenure', 'churn_history', 'satisfaction_scores' columns are available in the dataset
    # df['network_type'] = ...
    # df['customer_tenure'] = ...
    # df['churn_history'] = ...
    # df['satisfaction_scores'] = ...

    # Additional domain-specific features:
    df['issue_type'] = df['issue description'].apply(lambda x: 'Network' if 'network' in x.lower() else 'Other')

    # You can add more domain-specific features based on the telecommunication dataset

    return df
