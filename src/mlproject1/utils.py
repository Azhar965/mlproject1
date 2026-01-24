import os
import sys
from src.mlproject1.exception import CustomException
from src.mlproject1.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

print(f"DEBUG: Using user='{user}', host='{host}'")  # Verify .env

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
            
        )
        logging.info(f"Connection is established:{mydb}")
        df=pd.read_sql('Select * from students',mydb)
        print(df.head())
        

        return df


    except Exception as ex:
        raise CustomException (ex,sys)
    