# retraining/retrain.py

import mlflow
from models.topic_modeling import load_bertopic_model, train_bertopic_model
from feature_engineering.main_feature_engineering import run_feature_engineering

def retrain_model(existing_model_path, new_data_path, updated_model_path):
    # Load the existing BERTopic model
    existing_model = load_bertopic_model(existing_model_path)

    # Load and preprocess new data
    new_data = run_feature_engineering(new_data_path)

    # Retrain the model with new data
    updated_model = train_bertopic_model(new_data)

    # Save the updated model with MLflow
    with mlflow.start_run():
        mlflow.pyfunc.log_model("model", python_model=updated_model, artifacts={})
        mlflow.log_params({"language": "english", "top_n_words": 5})
        # ... other hyperparameters

    print("Model retraining completed successfully.")

if __name__ == "__main__":
    # Specify paths for existing model, new data, and updated model
    existing_model_path = "path/to/existing_model"
    new_data_path = "path/to/new_data.csv"
    updated_model_path = "path/to/updated_model"

    # Retrain the model
    retrain_model(existing_model_path, new_data_path, updated_model_path)
