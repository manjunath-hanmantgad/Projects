# feature_engineering/categorical_features.py

from sklearn.preprocessing import OneHotEncoder

def encode_categorical_features(df, columns_to_encode):
    encoder = OneHotEncoder(sparse=False, drop='first')
    encoded_features = encoder.fit_transform(df[columns_to_encode])
    encoded_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names_out(columns_to_encode))
    df = pd.concat([df, encoded_df], axis=1).drop(columns=columns_to_encode)
    return df
