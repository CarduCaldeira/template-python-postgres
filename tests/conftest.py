import pytest
from faker import Faker

from source.db import create_database_connection


#scope = module inicializa db_connection para para cada modulo testado
@pytest.fixture(scope='module')
def db_connection():

    connection = create_database_connection()
    yield connection
    connection.close()

#scope = function inicializa create_fake_news para para cada função testado
@pytest.fixture(scope='function')
def create_fake_news():

    lists = []
    news = []
    fake = Faker()
    
    news.append(fake.name())
    news.append(fake.sentence(nb_words=6))
    news.append(fake.paragraph(nb_sentences=3))
    news.append(fake.url())
    news.append(fake.image_url())
    news.append(fake.date_time_this_year())
    news.append(fake.text(max_nb_chars=2000))
    news.append(", ".join(fake.words(nb=5)))
    news.append(fake.company())
    news.append(fake.boolean())
    news.append(fake.boolean())
    news.append(fake.boolean())

    lists.append(tuple(news))
    
    return lists
