import pytest

from source.db import insert_list_database


@pytest.mark.db
def test_insert_database(db_connection, create_fake_news):
    
    fake_list = create_fake_news
    id = insert_list_database(fake_list)[0]

    cursor = db_connection.cursor()
    cursor.execute("""SELECT author, title, description, 
                   url, image_url, publication_date, 
                   content, tags, source, query0, query1, query2 
                   FROM raw_db.news WHERE id = %s;""", (id,))
    result = cursor.fetchall()
    cursor.close()

    assert result == fake_list
