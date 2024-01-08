# src/extraction/data_extraction.py
import pandas as pd
import logging
from prefect import task, Flow
from database.db_connection import create_db_engine
from database.query_builder import build_select_all_query

# Create a logger
logger = logging.getLogger(__name__)

@task
def extract_data_from_db(table_name, cache_path="data_cache.pkl"):
    try:
        # Attempt to load data from cache
        data = pd.read_pickle(cache_path)
        logger.info("Data loaded from cache.")
    except FileNotFoundError:
        try:
            # If cache not found, fetch data from the database
            engine = create_db_engine()
            query = build_select_all_query(table_name)
            data = pd.read_sql(query, engine)
            # Save data to cache for future use
            data.to_pickle(cache_path)
            logger.info("Data loaded from the database and saved to cache.")
        except Exception as e:
            logger.error(f"Error fetching data from the database: {e}")
            data = None  # Set data to None to indicate an error

    return data

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Define Prefect flow
with Flow("data_extraction_flow") as flow:
    table_name = "source_table"  # Update with your actual table name
    data = extract_data_from_db(table_name)

# Run the Prefect flow when the script is executed directly
if __name__ == "__main__":
    flow.run()
