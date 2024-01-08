# Machine Learning Application with PostgreSQL Integration

## Overview
This project demonstrates the development of a machine learning application with PostgreSQL integration for multi-class classification tasks. The application extracts data from a PostgreSQL database, performs data preprocessing, and trains a machine learning model for classification.

## Project Structure

project_root/
|-- src/
| |-- database/
| | |-- db_connection.py
| | |-- query_builder.py
| |-- preprocessing/
| | |-- data_preprocessing.py
| |-- modeling/
| | |-- train_model.py
| | |-- evaluate_model.py
| |-- extraction/
| | |-- data_extraction.py
|-- scripts/
| |-- extract_data.py
| |-- train_and_evaluate_model.py
|-- config/
| |-- config.yaml
|-- requirements.txt


1. Install dependencies:

pip install -r requirements.txt

2. Set up PostgreSQL database and configure environment variables.

## Usage

Extract Data
Run the data extraction script to retrieve data from the PostgreSQL database:

bash
python scripts/extract_data.py