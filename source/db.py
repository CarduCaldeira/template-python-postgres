from typing import List, Tuple

import psycopg2

from source.config import config


def create_database_connection() -> psycopg2.extensions.connection:

    params = config()
    print('Connecting to the postgreSQL database ...')
    connection = psycopg2.connect(**params)

    return connection

def insert_list_database(sql_query: str, data_list: List[Tuple]) -> None:
     
    connection = create_database_connection()
    cursor = connection.cursor()

    cursor.executemany(sql_query, data_list)

    connection.commit()

    cursor.close()
    connection.close()