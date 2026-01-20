import psycopg2


def create_movies_table():
    conn = psycopg2.connect(
        dbname='djangotraining',
        user='djangouser',
        password='secret',
        host='localhost'
    )

    try:
        with conn.cursor() as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS ex00_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INTEGER PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );""")

            conn.commit()
            context = {'status': 'OK', 'text': 'Table ‘ex00_movies’ successfully created!'}

    except Exception as e:
        context = {'status': 'KO', 'text': f'Error creating table: {e}'}
    finally:
        conn.close()
    return context
