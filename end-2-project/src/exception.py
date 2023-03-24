# creating custom exception

import sys 
import os
from src.logger import logging

# create function of error details

def error_message_detail(error,error_detail):
    '''contains detail about the error'''
    # we need the exe_tb which gives granular info about where line error is occuring
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    # define the error message aka error details here
    error_message = "Error occured in python script name [{0}] line number [{1}] error message is [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    # we need file name
     # this gives us filename
    
    
    return error_message
# creating custom exception class 

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message) # inheriting the custom class
        self.error_message=error_message_detail(error_message,error_detail=error_detail) # calling from the function defined above
        # the custom error message is initialised to error_detail
        
    # inheriting str function
    
    def __str__(self):
        '''used for printing custom error message'''
        
        return self.error_message 
    
if __name__ == "__main__":
    
    try:
        a=1/0
    except Exception as e:
        logging.info("You are dividing by 0, so it is not correct.")
        raise CustomException(e,sys)
        