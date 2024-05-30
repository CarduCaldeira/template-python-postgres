from typing import List, Tuple

import psycopg2

from source.config import config


def create_database_connection():

    params = config()
    print('Connecting to the postgreSQL database ...')
    connection = psycopg2.connect(**params)

    return connection

def insert_list_database(data_list: List[Tuple]):
     
    connection = create_database_connection()
    cursor = connection.cursor()
    inserted_ids = []

    for data in data_list:
        cursor.execute("""
            INSERT INTO raw_db.news (
                author, title, description, url, image_url, publication_date,
                content, tags, source, query0, query1, query2
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
        RETURNING id;
        """, data)
        inserted_id = cursor.fetchone()[0]
        inserted_ids.append(inserted_id)

    connection.commit()

    cursor.close()
    connection.close()

    return inserted_ids