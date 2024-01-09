# src/database/data_retrieval.py
import pandas as pd
from sqlalchemy import create_engine
import mlflow
from mlflow.tracking import MlflowClient
import os

def retrieve_new_data(engine, query):
    # Load the latest run's artifacts path from MLflow
    latest_run_id = get_latest_mlflow_run_id()
    artifacts_path = get_mlflow_run_artifacts_path(latest_run_id)

    # Define the file path for storing the retrieved data
    data_path = os.path.join(artifacts_path, "new_data.csv")

    # Query new data from PostgreSQL
    new_data = pd.read_sql(query, engine)

    # Save the retrieved data to a CSV file
    new_data.to_csv(data_path, index=False)

    # Log the data retrieval artifact in MLflow
    mlflow.log_artifact(data_path, artifact_path="data")

def get_latest_mlflow_run_id():
    client = MlflowClient()
    runs = client.search_runs(order_by=["start_time desc"], limit=1)
    return runs.iloc[0].info.run_id

def get_mlflow_run_artifacts_path(run_id):
    client = MlflowClient()
    run_info = client.get_run(run_id)
    return run_info.info.artifact_uri
