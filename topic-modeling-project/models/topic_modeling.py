# models/topic_modeling.py

import mlflow
import mlflow.pyfunc
from bertopic import BERTopic
from bertopic.vectorizer import CountVectorizer, OnlineCountVectorizer  # Correct import for vectorizers
from preprocessing.text_preprocessing import preprocess_text
from mlflow.tracking import MlflowClient
from sklearn.metrics import silhouette_score, pairwise_distances
from gensim.models import CoherenceModel
from gensim.corpora import Dictionary
from itertools import product

# Additional imports for UMAP and HDBSCAN
from umap import UMAP
from hdbscan import HDBSCAN

# Other import statements remain unchanged

# Function to fit and evaluate BERTopic model
def fit_evaluate_bertopic(train_df, val_df, st_model, vectorizer, text_column, umap_params, hdbscan_params, sentence_model_params, vectorizer_params, bertopic_params):
    # Initialize UMAP and HDBSCAN models with specified parameters
    umap_model = UMAP(**umap_params)
    hdbscan_model = HDBSCAN(**hdbscan_params)

    # Initialize BERTopic model with specified parameters
    topic_model = BERTopic(
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        sentence_model=st_model,
        vectorizer=vectorizer,
        top_n_words=bertopic_params['top_n_words'],
        language=bertopic_params['language'],
        calculate_probabilities=bertopic_params['calculate_probabilities'],
        verbose=bertopic_params['verbose']
    )

    # Generate topics on the training set
    topics, _ = topic_model.fit_transform(train_df[text_column])

    # ... (rest of the function remains unchanged)

    # Evaluate the model on the validation set
    val_topics, _ = topic_model.transform(val_df[text_column])

    # Calculate silhouette score as the evaluation metric
    val_silhouette_score = calculate_evaluation_metric(val_topics, val_df['label_column'])  # replace 'label_column' with the actual label column

    # Log the evaluation metric
    mlflow.log_metrics({"val_silhouette_score": val_silhouette_score})

# Function to calculate evaluation metric on the validation set
def calculate_evaluation_metric(val_topics, val_labels):
    # You can choose any evaluation metric relevant to your task
    # For example, silhouette score for clustering tasks
    silhouette_metric = silhouette_score(val_topics, val_labels)
    return silhouette_metric

# Function to generate all combinations of hyperparameters from a given space
def generate_param_combinations(param_space):
    param_names = list(param_space.keys())
    param_values = list(param_space.values())

    # Generate all combinations using itertools.product
    param_combinations = [dict(zip(param_names, values)) for values in product(*param_values)]

    return param_combinations

# Hyperparameter space for UMAP
umap_params_space = {
    'n_components': [5, 10],
    'n_neighbors': [5, 10],
    'min_dist': [0.1, 0.5],
    'metric': ['cosine', 'euclidean']
}

# Hyperparameter space for HDBSCAN
hdbscan_params_space = {
    'min_cluster_size': [5, 10],
    'min_samples': [1, 5],
    'metric': ['euclidean', 'manhattan']
}

# Hyperparameter space for BERTopic
bertopic_params_space = {
    'top_n_words': [5, 10],
    'language': ['english'],
    'calculate_probabilities': [True, False],
    'verbose': [True, False]
}

# Experiment with different sentence transformer models and vectorizers
for st_model in sentence_transformer_models:
    for vectorizer in vectorizers:
        for text_column in text_columns:
            # Hyperparameter tuning logic
            best_umap_params, best_hdbscan_params, best_bertopic_params = None, None, None
            best_metric = float('-inf')

            for umap_params in generate_param_combinations(umap_params_space):
                for hdbscan_params in generate_param_combinations(hdbscan_params_space):
                    for bertopic_params in generate_param_combinations(bertopic_params_space):
                        # Fit and evaluate BERTopic with current hyperparameters
                        fit_evaluate_bertopic(train_df, val_df, st_model, vectorizer, text_column, umap_params, hdbscan_params, sentence_model_params, vectorizer_params, bertopic_params)

                        # Calculate silhouette score as the evaluation metric on validation set
                        val_silhouette_score = calculate_evaluation_metric(val_topics, val_df['label_column'])  # replace 'label_column' with the actual label column

                        # Check if current hyperparameters result in a better metric
                        if val_silhouette_score > best_metric:
                            best_metric = val_silhouette_score
                            best_umap_params = umap_params
                            best_hdbscan_params = hdbscan_params
                            best_bertopic_params = bertopic_params

            # Use the best hyperparameters to fit and evaluate the final model
            fit_evaluate_bertopic(train_df, val_df, st_model, vectorizer, text_column, best_umap_params, best_hdbscan_params, sentence_model_params, vectorizer_params, best_bertopic_params)

# End of script
