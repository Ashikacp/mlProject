'''Data ingestion is the process of acquiring and importing data from various sources into a system for further processing, analysis, and storage. '''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass    #used to directly define class variable

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

@dataclass #This decorator automatically generates special methods like __init__() for the class, based on the class attributes
class DataIngestionConfig:  #This class holds configuration paths for datafiles. It's used to specify where the train,test,raw datafiles should be stored

    train_data_path: str = os.path.join('artifacts', 'train.csv')  
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:

    def __init__(self): 
        self.ingestion_config=DataIngestionConfig()  #Initializes an instance of DataIngestionConfig and assigns it to self.ingestion_config.
    
    def initiate_data_ingestion(self):  
        logging.info("Entered the data ingestion method/component")

        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) 

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split is initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("ingestion of the data is completed ")
            
            return self.ingestion_config.train_data_path,self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == '__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    logging.info(f'train_data is {train_data},test_data is {test_data},')

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

            




