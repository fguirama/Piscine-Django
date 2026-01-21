from ex00.sql import connect_postgres


def remove_sql_data(n, title):
    conn = connect_postgres()
    if not conn:
        return {'status': 'KO', 'text': 'Error connecting to database'}

    try:
        cur = conn.cursor()
        cur.execute('DELETE FROM ex0%s_movies WHERE title = %s;', (n, title))
        deleted_rows = cur.rowcount
        if deleted_rows:
            context = {'status': 'OK', 'text': 'Data removed successfully!'}
        else:
            context = {'status': 'OK', 'text': 'No data found to remove!'}
        conn.commit()
    except Exception as e:
        context = {'status': 'KO', 'text': f'Error removing data: {e}'}
    finally:
        conn.close()
    return context

