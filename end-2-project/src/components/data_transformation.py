# contains code related to feature engineering.
# do feature engineering
# deal with categorical features
# missing values
import os 
import sys 
from dataclasses import dataclass
import numpy as np
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
# import custom exception and logger
from src.exception import CustomException
from src.logger import logging

#creating base class which will handle data transformation
@dataclass
class DataTransformationConfig:
    '''class created to handle inputs and requirements'''
    preprocessor_obj_file_path=os.path.join('artifacts', "preprocessor.pkl") #this will create a preprocessor pickle file which contains preprocessed objects

class DataTransformation:
    '''main function performing data transformation'''
    def __init__(self):
        '''calling data transformation config'''
        self.data_transformation_config=DataTransformationConfig()
    def get_data_transformer_object(self):
        '''function to create pickle files for converting features categorical to numerical
        and do some feature engineering.'''
        try:
            numerical_columns=["writig_score","reading_Score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median"))
                    ("scaler",StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")) # handling missing values
                    ("one_hot_encoder", OneHotEncoder()), # for handling categorical features and converting them to numerical features
                    ("scaler", StandardScaler()) # perform scaling
                ]
            )
            logging.info("Standard scaling completed")
            logging.info("Categorical columns encoding completed")
            logging.info(f"Categorical columns:", {categorical_columns})
            logging.info(f"Numerical columns:", {numerical_columns})

            # combine categorical columns and numercial columns
            # using columntransformer from sklearn
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", numerical_pipeline,numerical_columns)
                    ("cat_pipeline", cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
    
    # after getting data transformation object 
    # initialse the data transformation 
    
    def initiate_data_transformation(self,train_path, test_path):
        try:
            # read training data 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read Train and test data completed.")
            logging.info("Obtaining preprocessing object starting")
            preprocessor_obj= self.get_data_transformer_object()
            # creating target column
            target_column_name="math_score" # this is the label to predict
            numerical_columns = ["writing_score", "reading_score"]
            # giving here X and y
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df=train_df[target_column_name]
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Applying preprocessing function now.")
            
            # saving as array objects
            # line numbers 95 - 103
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_test_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            # to save the object
            # file_path and actal object
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj
            )
            logging.info("Saved preprocessed objects as arrays.")
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            return CustomException(e,sys)
            
            