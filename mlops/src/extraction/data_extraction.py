# src/extraction/data_extraction.py
import pandas as pd
import logging
from prefect import task
from database.db_connection import create_db_engine
from database.query_builder import build_select_all_query

# Create a logger
logger = logging.getLogger(__name__)

@task
def extract_data_from_db(table_name, cache_path="data_cache.pkl"):
    """
    Extracts data from a PostgreSQL database table. Attempts to load data from a local cache
    and fetches from the database if the cache is not found.

    Parameters:
        table_name (str): The name of the database table.
        cache_path (str, optional): The path to the local cache file. Defaults to "data_cache.pkl".

    Returns:
        pd.DataFrame: The extracted data.

    Raises:
        FileNotFoundError: If the cache file is not found.
        Exception: If there is an error fetching data from the database or loading the cache.
    """
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
            # Handle any database-related exceptions
            logger.error(f"Error fetching data from the database: {e}")
            data = None  # Set data to None to indicate an error

    return data
