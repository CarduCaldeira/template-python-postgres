import psycopg2
from config import config

def create_database():
    
    params = config()
    print('Connecting to the postgreSQL database ...')
    connection = psycopg2.connect(**params)

    # create a cursor
    cursor = connection.cursor()
    print('PostgreSQL database version: ')
        
    try:
        # Insere um registro na tabela
        cursor.execute("CREATE TABLE t1 (id int)")
        cursor.execute("INSERT INTO t1 (id) VALUES (5)")

        # Commit da transação
        connection.commit()

        print("Registro inserido com sucesso!")

    except psycopg2.Error as e:
        print("Erro ao inserir o registro:", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()