from ex00.sql import connect_postgres


def create_movies_table(exersice):
    conn = connect_postgres()
    if not conn:
        return {'status': 'KO', 'text': 'Error connecting to database'}

    try:
        with conn.cursor() as cursor:
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS ex0{exersice}_movies (
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
