# data_preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def handle_missing_values(data):
    """
    Handle missing values in the dataset.

    Parameters:
    - data: Pandas DataFrame

    Returns:
    - data: Pandas DataFrame with missing values handled
    """
    data.dropna(inplace=True)
    return data

def handle_categorical_variables(data):
    """
    Handle categorical variables in the dataset (if applicable).

    Parameters:
    - data: Pandas DataFrame

    Returns:
    - data: Pandas DataFrame with categorical variables handled
    """
    # No categorical variables to handle in the Iris dataset
    return data

def feature_scaling(data):
    """
    Perform feature scaling on numerical features in the dataset.

    Parameters:
    - data: Pandas DataFrame

    Returns:
    - data: Pandas DataFrame with feature scaling applied
    """
    scaler = StandardScaler()
    numerical_features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    data[numerical_features] = scaler.fit_transform(data[numerical_features])
    return data

def handle_outliers(data):
    """
    Handle outliers in the dataset (if applicable).

    Parameters:
    - data: Pandas DataFrame

    Returns:
    - data: Pandas DataFrame with outliers handled
    """
    # Note: Implementation of outlier handling depends on the nature of the data

    return data

def data_splitting(data, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    Parameters:
    - data: Pandas DataFrame
    - test_size: Proportion of the dataset to include in the test split (default is 0.2)
    - random_state: Seed for random number generation (default is 42)

    Returns:
    - train_data: Pandas DataFrame - Training set
    - test_data: Pandas DataFrame - Testing set
    """
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)
    return train_data, test_data
