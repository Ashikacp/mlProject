import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig():
    trained_model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer():

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_arry,test_arry):

        try:
            logging.info("split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_arry[:,:-1], #take all columns except lastcolumn(ie:math_score)
                train_arry[:,-1],  #take lastcolumn(math_score)
                test_arry[:,:-1],
                test_arry[:,-1],
            )

            #dictionary of models
            models={
                "Random Forest": RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Linear Regression" : LinearRegression(),
                "KNeighbors Regression" : KNeighborsRegressor(),
                "XGB Regression" : XGBRegressor(),
                "CatBoost Regression" :CatBoostRegressor(verbose=False),
                "AdaBoost Regression":AdaBoostRegressor()
            } 

            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name] #it will pick the o/p of best_model_name from the models

            if best_model_score < 0.6:
                raise CustomException("No best model found")
            
            logging.info(f"Found the best model on both training and testing dataset")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model #dumping the best model in model.pkl file
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square


        except Exception as e:
            raise CustomException(e,sys)

