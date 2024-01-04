# feature_engineering/feature_scaling.py

from sklearn.preprocessing import StandardScaler

def scale_numerical_features(df, columns_to_scale):
    scaler = StandardScaler()
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    return df
