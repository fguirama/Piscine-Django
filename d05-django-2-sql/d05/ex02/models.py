def instert_sql_data(conn, cursor, n):
    status = []
    movies = [
        (1, 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
        (2, 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
        (3, 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
        (4, 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        (5, 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        (6, 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        (7, 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11'),
    ]

    query = f'INSERT INTO ex0{n}_movies (episode_nb, title, director, producer, release_date) VALUES (%s, %s, %s, %s, %s);'

    for movie in movies:
        try:
            cursor.execute(query, movie)
            conn.commit()
            status.append({'status': 'OK', 'text': f'Insert {movie[1]} successfully!'})
        except Exception as e:
            conn.rollback()
            status.append({'status': 'KO', 'text': f'Error inserting data: {e}'})

    return {'statuses': status}


def get_sql_data(_, cursor, n):
    cursor.execute('SELECT * FROM ex0%s_movies ORDER BY episode_nb;', (n, ))
    rows = cursor.fetchall()
    return {'movies': rows, 'status': 'OK'}
