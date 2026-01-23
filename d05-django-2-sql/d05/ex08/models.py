def create_planets_table(conn, cursor, _):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS ex08_planets (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        climate VARCHAR,
        diameter INTEGER,
        orbital_period INTEGER,
        population BIGINT,
        rotation_period INTEGER,
        surface_water REAL,
        terrain VARCHAR(128)
    );''')
    conn.commit()
    return {'status': 'OK', 'text': f'Table ‘ex08_planets’ successfully created!'}


def create_people_table(conn, cursor, _):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS ex08_people (
        id SERIAL PRIMARY KEY,
        name VARCHAR(64) UNIQUE NOT NULL,
        birth_year VARCHAR(32),
        gender VARCHAR(32),
        eye_color VARCHAR(32),
        hair_color VARCHAR(32),
        height INTEGER,
        mass REAL,
        homeworld VARCHAR(64),
        FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
    );''')
    conn.commit()
    return {'status': 'OK', 'text': f'Table ‘ex08_people’ successfully created!'}


def instert_sql_data(conn, cursor, _, name, columns):
    with open(f'ex08/{name}.csv') as f:
        cursor.copy_from(
            f,
            f'ex08_{name}',
            columns=columns,
            sep='\t',
            null='NULL'
        )
    conn.commit()
    return {'status': 'OK', 'text': f'Insert data in ex08_{name} successfully!'}


def get_sql_data(_1, cursor, _2):
    cursor.execute('''
        SELECT people.name, planet.name AS homeworld, planet.climate
        FROM ex08_people people
            JOIN ex08_planets planet ON people.homeworld = planet.name
        WHERE planet.climate LIKE '%windy%'
        ORDER BY people.name ASC;
    ''')
    peoples = cursor.fetchall()
    return {'peoples': peoples, 'status': 'OK'}
