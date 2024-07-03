# reading data from a particular datasource
import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv") 
    # artifacts is a directory where we are storing all these csv files
    # creating a path in which data will bestored using dataingestion method

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            if not os.path.exists(self.ingestion_config.train_data_path):
                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path))
            # os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exists_ok = True)
            # exists_ok_true means if the file is already created then dont delete and create it 
            # again
            # self.ingestion_config.train_data_path is the path to the training data file
            # os.path.dirname returns directory name of the path
            #  os.makedirs makes dir if it is not present and gives an error if dir is already present
            # but in this case since we have exists_ok = True hence it wont give an error even if
            # dir is already present
            # since exists ok is not supprted in older python versions hence we can manually check whether file is present or not

            # converting the dir to a csv file
            df.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)

            logging.info("train test split initiated")

            train_set,test_set = train_test_split(df,test_size = 0.2,random_state = 42)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)

            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            # here the storing of data into the empty csv file occurs

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
