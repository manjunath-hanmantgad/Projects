# src/database/db_connection.py
import os
import logging
from sqlalchemy import create_engine, pool
import yaml

# Create a logger
logger = logging.getLogger(__name__)

def load_config():
    """
    Load configuration parameters from the 'config.yaml' file.

    Returns:
        dict: A dictionary containing configuration parameters.
    """
    with open("config.yaml", "r") as config_file:
        return yaml.safe_load(config_file)

def create_db_engine():
    """
    Create an SQLAlchemy engine for connecting to a PostgreSQL database with connection pooling.

    Returns:
        sqlalchemy.engine.Engine: An SQLAlchemy engine object.

    Raises:
        Exception: If there is an error creating the database engine.
    """
    try:
        # Retrieve database credentials from environment variables
        username = os.environ.get("DB_USERNAME")
        password = os.environ.get("DB_PASSWORD")
        host = os.environ.get("DB_HOST")
        database_name = os.environ.get("DB_NAME")
        
        # Retrieve connection pooling parameters from the config file
        config = load_config()
        pool_size = config["database"].get("pool_size", 5)
        max_overflow = config["database"].get("max_overflow", 10)

        # Build the connection string
        connection_string = f"postgresql://{username}:{password}@{host}/{database_name}"

        # Use SQLAlchemy's connection pooling
        engine = create_engine(connection_string, poolclass=pool.QueuePool, pool_size=pool_size, max_overflow=max_overflow)
        
        logger.info("Database engine with connection pooling created successfully.")
        return engine
    except Exception as e:
        logger.error(f"Error creating database engine: {e}")
        return None
