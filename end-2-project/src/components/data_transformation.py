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
