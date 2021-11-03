# Read the CSV file using the spark dataframe reader

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

# create a schema so that structfield can be defined.
# structfield is ROWS of the table

circuits_schema = StructType(fields=[StructField("circuitId", IntegerType(), False),
                                     StructField("circuitRef", StringType(), True),
                                     StructField("name", StringType(), True),
                                     StructField("location", StringType(), True),
                                     StructField("country", StringType(), True),
                                     StructField("lat", DoubleType(), True),
                                     StructField("lng", DoubleType(), True),
                                     StructField("alt", IntegerType(), True),
                                     StructField("url", StringType(), True)
                                     
                                     
# create a dataframe to read in the csv data
circuits_df = spark.read.option("header", True).schema(circuits_schema).csv("/mnt/adlstorage/raw/circuits.csv")


#  Select only the required columns

from pyspark.sql.functions import col

# use df.select method from SPARK api to select the columns which are of use.
circuits_selected_df = circuits_df.select(col("circuitId"), col("circuitRef"), col("name"), col("location"), col("country"), col("lat"), col("lng"), col("alt"))

# Rename the columns as required

circuits_renamed_df = circuits_selected_df.withColumnRenamed("circuitId", "circuit_id") \
.withColumnRenamed("circuitRef", "circuit_ref") \
.withColumnRenamed("lat", "latitude") \
.withColumnRenamed("lng", "longitude") \
.withColumnRenamed("alt", "altitude")


# Add ingestion date to the dataframe

from pyspark.sql.functions import current_timestamp

# contains the dataframe with the ingested timestamp
circuits_final_df = circuits_renamed_df.withColumn("ingestion_date", current_timestamp())


# Write data to datalake as parquet
circuits_final_df.write.mode("overwrite").parquet("/mnt/adlstorage/processed/circuits")

display(spark.read.parquet("/mnt/adlstorage/processed/circuits"))