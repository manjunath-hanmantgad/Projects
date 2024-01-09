# main.py
import pandas as pd
from src.database.db_connection import create_db_engine
from src.database.query_builder import build_select_all_query
from src.extraction.data_extraction import extract_data_from_db
from src.preprocessing.data_preprocessing import handle_missing_values, handle_categorical_variables, feature_scaling, handle_outliers, data_splitting

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

    # Data Splitting
    train_data, test_data = data_splitting(data)


if __name__ == "__main__":
    main()
