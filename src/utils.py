'''utils.py file  will be having the common functionality which the entire project can use'''

import os
import sys
import numpy as np
import pandas as pd
import dill  #dill is used for serializing the Python object  into a binary file.

from src.exception import CustomException


def save_object(file_path,obj): #file_path:-the location where the object should be saved, and obj: the object to be serialized.
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj) #The object is saved using dill.dump() to serialize and save it as a binary file.

            
    except Exception as e:
        raise CustomException(e,sys)