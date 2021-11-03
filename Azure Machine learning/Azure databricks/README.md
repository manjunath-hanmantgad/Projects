The project contains Azure databricks , Azure data lake storage Gen2 , Azure data factory.


The flow of project is:

Ingest data from API -> Mount the data into ADLS Gen2 as RAW data -> Data is stored in ADLS ingest layer -> Transform this data -> data is stored in Presentation layer of ADLS Gen2 -> Using Power BI to perfrom analysis


To construct the flow of data I will use Azure data factory pipelines.
