# contains code for reading the data.
# can be from database as well
# local data source i.e storing database in local and fetching from here.

import os 
import sys 
# required for custom logger and exception
from src.exception import CustomException
from src.logger import logging
# for custom exception and logging.
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
# for train test splitting
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig,ModelTrainer
# required for inputs to save raw data , test/train data
# this class is used for that 
@dataclass
class DataIngestionConfig():
    # using dataclass we can directly define data types
    train_data_path: str=os.path.join('artifacts','train.csv') # trainig path where train.csv will be saved
    test_data_path: str=os.path.join('artifacts','test.csv') # testing path where test.csv will be saved
    raw_data_path: str=os.path.join('artifacts','data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # this will contain 3 paths
        # and now when we call these 3 paths of train test raw data get saved into DataIngestion class.
        
    def initiate_data_ingestion(self):
        """Used for reading the data"""
        logging.info("Begin the data ingestion method")
        try:
            df=pd.read_csv(r'D:\development\Projects\end-2-project\notebook\data\stud.csv')
            # instead of this I can also use NoSQL db to load data
            logging.info("Reading the raw dataset.")
            # directories for artifacts
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)
            logging.info("Initialising train test split")
            train_set, test_set = train_test_split(df,test_size=0.27,random_state=9)
            logging.info("Splitting is done and train and test data is getting saved to train csv and test csv into artifacts folder")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)
            logging.info("Data ingestion is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
# running locally

# here we combined data ingestion and data transformation
# if data validation was there then combine that as well here.
if __name__=="__main__":
    obj=DataIngestion()# creates artifacts folder
    #obj.initiate_data_ingestion()
    train_data, test_data = obj.initiate_data_ingestion()
    data_transformation=DataTransformation() # this will call from data transformation
    # calling data transformation
    #data_transformation.initiate_data_transformation(train_data,test_data)
    train_arr,test_arr, = data_transformation.initiate_data_transformation(train_data,test_data)
    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
    
    


