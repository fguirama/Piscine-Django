import psycopg2
from psycopg2.extras import RealDictCursor


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


def make_query(function, n, error='', **kwargs):
    conn = connect_postgres()
    if not conn:
        return {'status': 'KO', 'text': 'Error connecting to database'}

    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            context = function(conn, cursor, n, **kwargs)

    except Exception as e:
        context = {'status': 'KO', 'text': f'Error {error}: {e}'}
    finally:
        conn.close()
    return context
