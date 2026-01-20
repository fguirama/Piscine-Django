import psycopg2


def connect_postgres():
    try:
        return psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='localhost'
        )
    except psycopg2.Error:
        return None
