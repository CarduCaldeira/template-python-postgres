import os


def config():
       
    dict_param ={'dbname': os.getenv("DB_NAME"),
                'user': os.getenv("DB_USER"),
                'port': os.getenv("DB_PORT"),
                'password': os.getenv("DB_PASSWORD"),
                'host': os.getenv("DB_HOST")}
    
    return dict_param