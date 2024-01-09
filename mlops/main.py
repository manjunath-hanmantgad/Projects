# main.py
import pandas as pd
from src.database.db_connection import create_db_engine
from src.database.query_builder import build_select_all_query
from src.extraction.data_extraction import extract_data_from_db
from src.preprocessing.data_preprocessing import handle_missing_values, handle_categorical_variables, feature_scaling, handle_outliers, data_splitting
from src.feature_engineering.feature_engineering import create_interaction_terms, select_best_features

def main():
    # Connect to the database and retrieve data
    engine = create_db_engine()
    table_name = "source-table"
    query = build_select_all_query(table_name)
    data = extract_data_from_db(query, engine)

    # Data Preprocessing
    data = handle_missing_values(data)
    data = handle_categorical_variables(data)
    data = feature_scaling(data)
    data = handle_outliers(data)

    # Feature Engineering
    data = create_interaction_terms(data, interaction_degree=2)
    data = select_best_features(data, k=4)

    # Data Splitting
    train_data, test_data = data_splitting(data)

    # Now you can proceed with training and evaluating your machine learning model using train_data and test_data

if __name__ == "__main__":
    main()
