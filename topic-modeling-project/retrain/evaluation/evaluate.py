# evaluation/evaluate.py

from models.topic_modeling import load_bertopic_model
from feature_engineering.main_feature_engineering import run_feature_engineering
from scoring.scoring import generate_predictions  # Reuse the scoring pipeline for evaluation
from bertopic import BERTopic
from sklearn.metrics import silhouette_score, davies_bouldin_score
import numpy as np

def evaluate_model(model_path, new_data_path):
    # Load the BERTopic model
    model = load_bertopic_model(model_path)

    # Load and preprocess new data
    new_data = run_feature_engineering(new_data_path)

    # Generate predictions using the loaded model
    predictions = generate_predictions(model, new_data)

    # Evaluate coherence score
    coherence_score = model.get_coherence()

    # Evaluate perplexity (lower is better)
    perplexity = model.get_perplexity()

    # Evaluate silhouette score (higher is better)
    # Note: Requires a labeled dataset
    # silhouette = silhouette_score(new_data, labels)

    # Evaluate Davies-Bouldin score (lower is better)
    # Note: Requires a labeled dataset
    # davies_bouldin = davies_bouldin_score(new_data, labels)

    print(f"Coherence Score: {coherence_score}")
    print(f"Perplexity: {perplexity}")
    # Uncomment the lines below if you have labeled data for silhouette and davies_bouldin scores
    # print(f"Silhouette Score: {silhouette}")
    # print(f"Davies-Bouldin Score: {davies_bouldin}")

    print("Model evaluation completed successfully.")

if __name__ == "__main__":
    # Specify paths for the model and new data
    model_path = "path/to/trained_model"
    new_data_path = "path/to/new_data.csv"

    # Evaluate the model on new data
    evaluate_model(model_path, new_data_path)
