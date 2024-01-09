# train_model.py
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def select_model(model_name):
    """
    Select a machine learning model based on the given name.
    Supported models: 'RandomForest', 'SVM', 'KNN', 'DecisionTree'.

    Parameters:
    - model_name: Name of the model to select.

    Returns:
    - model: Selected machine learning model.
    """
    if model_name == 'RandomForest':
        return RandomForestClassifier(random_state=42)
    elif model_name == 'SVM':
        return SVC(random_state=42)
    elif model_name == 'KNN':
        return KNeighborsClassifier()
    elif model_name == 'DecisionTree':
        return DecisionTreeClassifier(random_state=42)
    else:
        raise ValueError(f"Unsupported model: {model_name}")

def train_and_evaluate_model(data, model_name):
    """
    Train and evaluate a machine learning model.

    Parameters:
    - data: Pandas DataFrame containing preprocessed data.
    - model_name: Name of the model to train.

    Returns:
    - model: Trained machine learning model.
    """
    # Extract features and target variable
    X = data.drop(columns=['target'])
    y = data['target']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model selection
    model = select_model(model_name)

    # Feature scaling (if applicable)
    # Add code for feature scaling here if needed

    # Hyperparameter tuning (if applicable)
    # Add code for hyperparameter tuning here if needed

    # Model training
    with mlflow.start_run():
        model.fit(X_train, y_train)

        # Cross-validation
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        mlflow.log_param("cross_val_scores", cv_scores.tolist())

        # Model evaluation
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        classification_rep = classification_report(y_test, y_pred, output_dict=True)

        # Log metrics
        mlflow.log_param("model_name", model_name)
        mlflow.log_param("accuracy", accuracy)
        mlflow.log_metrics({"precision": classification_rep['weighted avg']['precision'],
                            "recall": classification_rep['weighted avg']['recall'],
                            "f1-score": classification_rep['weighted avg']['f1-score']})

        # Log model
        mlflow.sklearn.log_model(model, f"model_{model_name}")

    return model

# Example usage:
# trained_model = train_and_evaluate_model(data, 'RandomForest')
