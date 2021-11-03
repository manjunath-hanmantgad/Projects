# Read the JSON file using the spark dataframe reader API
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
name_schema = StructType(fields=[StructField("forename", StringType(), True),
                                 StructField("surname", StringType(), True)
  
])

drivers_schema = StructType(fields=[StructField("driverId", IntegerType(), False),
                                    StructField("driverRef", StringType(), True),
                                    StructField("number", IntegerType(), True),
                                    StructField("code", StringType(), True),
                                    StructField("name", name_schema),
                                    StructField("dob", DateType(), True),
                                    StructField("nationality", StringType(), True),
                                    StructField("url", StringType(), True)  
])


drivers_df = spark.read \
.schema(drivers_schema) \
.json("/mnt/adlstorage01/raw/drivers.json")


# Rename columns and add new columns
# driverId renamed to driver_id
# driverRef renamed to driver_ref
# ingestion date added
# name added with concatenation of forename and surname


from pyspark.sql.functions import col, concat, current_timestamp, lit
drivers_with_columns_df = drivers_df.withColumnRenamed("driverId", "driver_id") \
                                    .withColumnRenamed("driverRef", "driver_ref") \
                                    .withColumn("ingestion_date", current_timestamp()) \
                                    .withColumn("name", concat(col("name.forename"), lit(" "), col("name.surname")))
                                    

#  Drop the unwanted columns
# name.forename
# name.surname
# url                                    

drivers_final_df = drivers_with_columns_df.drop(col("url"))       


#  Write to output to processed container in parquet format

drivers_final_df.write.mode("overwrite").parquet("/mnt/adlstorage01/processed/drivers")