from psycopg2.extras import DictCursor

from ex00.sql import connect_postgres


def instert_sql_data():
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]

    try:
        conn = connect_postgres()
        if not conn:
            return {'status': 'KO', 'text': 'Error connecting to database'}

        cur = conn.cursor()
        query = """INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date) VALUES (%s, %s, %s, %s, %s);"""

        for movie in movies:
            cur.execute(query, movie)
            conn.commit()

        cur.close()
        conn.close()

    except Exception as e:
        return {'status': 'KO', 'text': f'Error inserting data: {e}'}

    return {'status': 'OK', 'text': 'Data inserted successfully!'}


def get_sql_data():
    try:
        conn = connect_postgres()
        if not conn:
            return {'movies': [], 'status': 'KO', 'text': 'Error connecting to database'}
        cur = conn.cursor(cursor_factory=DictCursor)

        query = """SELECT * FROM ex02_movies ORDER BY episode_nb;"""

        cur.execute(query)
        rows = cur.fetchall()

        cur.close()
        conn.close()

    except Exception as e:
        return {'movies': [], 'status': 'KO', 'text': f'Error fetching data: {e}'}

    return {'movies': rows, 'status': 'OK'}
