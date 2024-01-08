# drift_calculation.py
import pandas as pd
from extraction.data_extraction import extract_data_from_db, calculate_data_drift

if __name__ == "__main__":
    """
    Calculates data drift by comparing new data with the baseline.
    The baseline is loaded from the saved CSV file.
    """
    try:
        # Define the table name
        table_name = "source-table"

        # Extract baseline data (run this once or periodically to update the baseline)
        baseline_data = pd.read_csv('baseline_data.csv')  # Load baseline data from the saved CSV

        # Extract new data (run this periodically or based on your monitoring schedule)
        new_data = extract_data_from_db(table_name)

        # Calculate and visualize data drift
        calculate_data_drift(baseline_data, new_data)

        print("Data drift calculation completed successfully.")
    except Exception as e:
        print(f"Error calculating data drift: {e}")
