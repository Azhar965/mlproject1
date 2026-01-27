from src.mlproject1.exception import CustomException
from src.mlproject1.logger import logging
import sys
from src.mlproject1.components.data_ingestion import DataIngestion
from src.mlproject1.components.data_ingestion import DataIngestionConfig
from src.mlproject1.components.data_transformation import DataTransformation,DataTransformationConfig
from src.mlproject1.components.model_trainer import ModelTrainer, ModelTrainerConfig


if __name__ == "__main__":
    logging.info("the execution has started...")


    try:
       # data_ingestion=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr, test_arr, _=data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        ## Model Training

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    
