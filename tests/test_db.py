import pytest

from source.db import insert_list_database


@pytest.mark.db
def test_insert_database(db_connection, create_fake_news):
    
    fake_list = create_fake_news

    sql_command = """
        INSERT INTO raw_db.news (
            author, title, description, url, image_url, publication_date,
            content, tags, source, query0, query1, query2
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    insert_list_database(sql_command, fake_list)

    cursor = db_connection.cursor()
    sql_select = "SELECT id FROM raw_db.news WHERE title IN %s;"

    titles = tuple([fake_list[0][1]])

    # Executando o comando 'SELECT'
    cursor.execute(sql_select, (titles,))
    id = cursor.fetchone()[0]
   
    cursor.close()

    assert id is not None