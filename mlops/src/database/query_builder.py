# src/database/query_builder.py
import logging

# Create a logger
logger = logging.getLogger(__name__)

def build_select_all_query(table_name):
    """
    Builds a simple SELECT query to retrieve all columns from a specified table.

    Parameters:
        table_name (str): The name of the table.

    Returns:
        str: The generated SELECT query.

    Raises:
        Exception: If there is an error building the query.
    """
    try:
        query = f"SELECT * FROM {table_name};"
        logger.info(f"SELECT query built for table '{table_name}'.")
        return query
    except Exception as e:
        # Handle any query building-related exceptions
        logger.error(f"Error building SELECT query: {e}")
        return None
