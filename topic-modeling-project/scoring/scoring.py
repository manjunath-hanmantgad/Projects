# scoring.py

import mlflow
from models.topic_modeling import load_bertopic_model
from feature_engineering.text_preprocessing import preprocess_text
from feature_engineering.main_feature_engineering import apply_feature_engineering

def load_and_preprocess_model(model_path, text):
    # Load BERTopic model using MLflow
    with mlflow.start_run():
        # Load the model using mlflow.pyfunc.load_model
        model = mlflow.pyfunc.load_model(model_path)

    # Preprocess text
    preprocessed_text = preprocess_text(text)

    return model, preprocessed_text

def generate_predictions(model, preprocessed_text):
    # Apply feature engineering steps if needed
    # For example, if your training pipeline applied additional feature transformations
    # such as calculating time-based features, apply those transformations here.

    # Feature engineering for scoring
    features = apply_feature_engineering(preprocessed_text)

    # Generate predictions using the loaded model
    # Add any additional post-processing steps if necessary
    predictions = model.transform([features])

    return predictions
