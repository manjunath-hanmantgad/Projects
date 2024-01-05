# main.py

import mlflow
from feature_engineering.main_feature_engineering import run_feature_engineering
from models.topic_modeling import train_bertopic_model
from utils.metrics import calculate_silhouette_score, calculate_coherence_score

def main():
    # Set MLflow experiment name
    mlflow.set_experiment("your_experiment_name")

    # Start MLflow run
    with mlflow.start_run():
        # Load and preprocess data (replace with your data loading logic)
        data_path = "data/processed/train_data.pkl"  # Adjust the path as needed
        train_data, val_data = run_feature_engineering(data_path)

        # Train BERTopic model
        model = train_bertopic_model(train_data)

        # Evaluate model on validation set
        val_silhouette_score = calculate_silhouette_score(val_data, model.get_labels())
        val_coherence_score = calculate_coherence_score(model, val_data['text_column'])

        # Log hyperparameters (replace with your actual hyperparameters)
        mlflow.log_param("language", "english")
        mlflow.log_param("top_n_words", 5)
        # Add more hyperparameters as needed

        # Log metrics
        mlflow.log_metric("silhouette_score", val_silhouette_score)
        mlflow.log_metric("coherence_score", val_coherence_score)

        # Log model artifact
        mlflow.pyfunc.log_model("model", python_model=model, artifacts={})

if __name__ == "__main__":
    main()
