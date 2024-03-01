import os
from dotenv import load_dotenv

def config():
       
    load_dotenv()

    dict_param ={'dbname': os.getenv("DB_NAME"),
                'user': os.getenv("DB_USER"),
                'password': os.getenv("DB_PASSWORD"),
                'host': os.getenv("DB_HOST")}
    
    return dict_param