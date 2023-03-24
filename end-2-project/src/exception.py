# creating custom exception

import sys 
import os 

# create function of error details

def error_message_detail(error,error_detail):
    '''contains detail about the error'''
    # we need the exe_tb which gives granular info about where line error is occuring
    _,_,exc_tb=error_detail.exc_info()
    # define the error message aka error details here
    error_message = "Error occured in python script name [{0}] line number [{1}] error message is [{2}]".format()
    # we need file name
    file_name = exc_tb.tb_frame.f_code.co_filename # this gives us filename
    file_name,exc_tb.tb_lineno,str(error)
    
    return error_message
# creating custom exception class 

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super.__init__(error_message) # inheriting the custom class
        self.error_message=error_message_detail(error_message,error_detail=error_detail) # calling from the function defined above
        # the custom error message is initialised to error_detail
        
    # inheriting str function
    
    def __str__(self):
        '''used for printing custom error message'''
        
        return self.error_message 
    