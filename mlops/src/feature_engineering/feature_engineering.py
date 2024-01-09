# feature_engineering.py
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import PolynomialFeatures

def create_interaction_terms(data, interaction_degree=2):
    """
    Create interaction terms up to a specified degree.

    Parameters:
    - data: Pandas DataFrame
    - interaction_degree: Degree of interaction terms (default is 2)

    Returns:
    - data: Pandas DataFrame with interaction terms added
    """
    poly = PolynomialFeatures(interaction_degree, include_bias=False)
    interaction_terms = poly.fit_transform(data.drop(columns=['target']))
    interaction_df = pd.DataFrame(interaction_terms, columns=poly.get_feature_names(data.columns[:-1]))
    data = pd.concat([data, interaction_df], axis=1)
    return data

def select_best_features(data, k=4):
    """
    Select the top k features using SelectKBest with ANOVA F-statistic.

    Parameters:
    - data: Pandas DataFrame
    - k: Number of top features to select (default is 4)

    Returns:
    - data: Pandas DataFrame with selected features
    """
    X = data.drop(columns=['target'])
    y = data['target']

    selector = SelectKBest(score_func=f_classif, k=k)
    X_selected = selector.fit_transform(X, y)

    # Get selected feature names
    selected_feature_names = X.columns[selector.get_support()]

    # Update the DataFrame with selected features
    data = pd.concat([data[['target']], pd.DataFrame(X_selected, columns=selected_feature_names)], axis=1)
    return data
