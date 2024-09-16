import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #strftime() is used to format the current date and time in a specific way.

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) #eg:/Users/your_name/project/logs/09_12_2024_13_45_22.log

os.makedirs(logs_path,exist_ok=True) #tries to create the directory specified by logs_path ,ie here it creates logs folder 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)






'''
#for testing
if __name__ == "__main__":
    logging.info("Logging has started")
  '''  
