# src/database/db_connection.py
import os
import logging
from sqlalchemy import create_engine, pool

# Create a logger
logger = logging.getLogger(__name__)

def create_db_engine():
    """
    Creates an SQLAlchemy engine for connecting to a PostgreSQL database.

    Returns:
        sqlalchemy.engine.Engine: An SQLAlchemy engine object.

    Raises:
        Exception: If there is an error creating the database engine.
    """
    try:
        username = os.environ.get("DB_USERNAME")
        password = os.environ.get("DB_PASSWORD")
        host = os.environ.get("DB_HOST")
        database_name = os.environ.get("DB_NAME")

        connection_string = f"postgresql://{username}:{password}@{host}/{database_name}"
        print(f"Using database: {database_name}")
        engine = create_engine(connection_string, poolclass=pool.QueuePool, pool_size=10, max_overflow=20)

        logger.info("Database engine created successfully.")
        return engine
    except Exception as e:
        # Handle any database connection-related exceptions
        logger.error(f"Error creating database engine: {e}")
        return None
