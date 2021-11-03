# this contains ingestion for JSON file

# Read the JSON file using the spark dataframe reader

constructors_schema = "constructorId INT, constructorRef STRING, name STRING, nationality STRING, url STRING"

constructor_df = spark.read \
.schema(constructors_schema) \
.json("/mnt/adlstorage01/raw/constructors.json")

# Drop unwanted columns from the dataframe

from pyspark.sql.functions import col
constructor_dropped_df = constructor_df.drop(col('url'))

# Rename columns and add ingestion date
from pyspark.sql.functions import current_timestamp
constructor_final_df = constructor_dropped_df.withColumnRenamed("constructorId", "constructor_id") \
                                             .withColumnRenamed("constructorRef", "constructor_ref") \
                                             .withColumn("ingestion_date", current_timestamp())
                                             
                                             
# Write output to parquet file

constructor_final_df.write.mode("overwrite").parquet("/mnt/adlstorage01/processed/constructors")                                             