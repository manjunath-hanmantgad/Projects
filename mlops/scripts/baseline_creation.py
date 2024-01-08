# baseline_creation.py
import pandas as pd
from extraction.data_extraction import extract_data_from_db

def create_baseline(table_name):
    """
    Creates a baseline dataset by extracting data from the database and saves it to a CSV file.

    Args:
        table_name (str): The name of the table from which data is extracted.
    """
    try:
        # Extract baseline data
        baseline_data = extract_data_from_db(table_name)

        # Save baseline data to a CSV file
        baseline_data.to_csv('baseline_data.csv', index=False)

        print("Baseline data created successfully.")
    except Exception as e:
        print(f"Error creating baseline data: {e}")

if __name__ == "__main__":
    # Define the table name
    table_name = "source-table"

    # Create and save the baseline data
    create_baseline(table_name)
