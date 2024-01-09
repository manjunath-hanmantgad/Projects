# src/modeling/model_scoring.py
import mlflow
import pandas as pd
from sklearn.externals import joblib  # For loading the trained model, adapt based on your model type
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc, roc_auc_score

def score_model(model_name, preprocessed_new_data, true_labels):
    # Retrieve the model path from MLflow
    model_path = f"runs:/{mlflow.active_run().info.run_id}/model_{model_name}"

    # Load the trained model
    loaded_model = mlflow.sklearn.load_model(model_path)

    # Make predictions on the preprocessed new data
    predicted_labels = loaded_model.predict(preprocessed_new_data)
    predicted_probabilities = loaded_model.predict_proba(preprocessed_new_data)[:, 1]  # For ROC and AUC

    # Calculate metrics
    accuracy = accuracy_score(true_labels, predicted_labels)
    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)
    conf_matrix = confusion_matrix(true_labels, predicted_labels)
    fpr, tpr, _ = roc_curve(true_labels, predicted_probabilities)
    roc_auc = auc(fpr, tpr)
    auc_score = roc_auc_score(true_labels, predicted_probabilities)

    # Log metrics in MLflow
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("roc_auc", roc_auc)

    # Additional logs
    mlflow.log_confusion_matrix(conf_matrix)
    mlflow.log_roc_curve(fpr, tpr)
    mlflow.log_artifact("your_additional_metrics.txt")  # Include any additional metrics

    return predicted_labels
