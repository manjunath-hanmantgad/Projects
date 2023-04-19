# used for training the ml model
# train different models
# get the metrics for the problem - accuracy , r sqaured etc
import os
import sys
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

# create config file

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    
class ModelTrainer():
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    def initiate_model_trainer(self,train_arr,test_arr,preprocessor_path):
        try:
            logging.info("Beginning the model training")
            logging.info("Splitting data into train and test")
            X_train,y_train,X_test,y_test = (
                train_arr[:,:-1],  # X-train# take out last column
                train_arr[:,-1], # y_train
                test_arr[:,:-1] , # X_test
                test_arr[:,-1] # y_test
            )
            # define the models here
            
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision tree": DecisionTreeRegressor(),
                "Linear regression": LinearRegression(),
                "K neighbours regression": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "Adaboost Regressor": AdaBoostRegressor()
            }
            model_report: dict= evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                               models=models)
            
            # get the best performing model 
            
            best_model_score = max(sorted(model_report.values()))
            
            # get best model name
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]
            
            if best_model_score < 0.6:
                raise CustomException("All model scores aare less than 0.6. Work on yur tuning.")
            
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
        except Exception as e:
            return CustomException(e,sys)
        
            