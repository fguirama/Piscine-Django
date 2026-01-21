def create_movies_table(conn, cursor, n):
    extra_fields = ''
    if n == 6:
        extra_fields = ''',
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP'''
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS ex0%s_movies (
        title VARCHAR(64) UNIQUE NOT NULL,
        episode_nb INTEGER PRIMARY KEY,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL {extra_fields}
    );''', (n, ))
    if n == 6:
        cursor.execute('''CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
        ''')
    conn.commit()
    return {'status': 'OK', 'text': f'Table ‘ex0{n}_movies’ successfully created!'}
