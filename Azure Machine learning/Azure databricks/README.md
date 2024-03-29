The project contains Azure databricks , Azure data lake storage Gen2 , Azure data factory.

Language used : Python , Spark , Spark SQL 

Analytic tool - Power BI


🟧  The flow of project is:

Ingest data from API -> Mount the data into ADLS Gen2 as RAW data -> Data is stored in ADLS ingest layer -> Transform this data -> data is stored in Presentation layer of ADLS Gen2 -> Using Power BI to perfrom analysis


To construct the flow of data I will use Azure data factory pipelines.


🌩️ Data Ingestion 

Steps involved in ingesting data :

↪️ Read the CSV file using the spark dataframe reader API

↪️ create a schema so that structfield can be defined.

↪️ create a dataframe to read in the csv data

↪️  Select only the required columns

↪️  Rename the columns as required

↪️  Add ingestion date and race_timestamp to the dataframe

↪️ Write data to datalake as parquet

------------------

🌩️ Databricks Workflows

(Instead of hardcoding create config or variables and invoke using %run command 📜)

↪️ Connect multiple notebooks toghether

↪️ Invoke single notebook from other notebook

↪️ Configure and run/schedule databricks jobs


-------------------------

🌩️ Incremental Data loading as compared to Full load.


------------------------

🌩️ Azure Data factory Pipelines 

The steps include:

↪️ Create data factory service

↪️ Linking data factory components

↪️ Creating data factory Pipelines

↪️ Creating triggers
