def create_movies_table(conn, cursor, n):
    cursor.execute('''CREATE TABLE IF NOT EXISTS ex0%s_movies (
        title VARCHAR(64) UNIQUE NOT NULL,
        episode_nb INTEGER PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
    );''', (n, ))
    conn.commit()
    return {'status': 'OK', 'text': 'Table ‘ex00_movies’ successfully created!'}
