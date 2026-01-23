def remove_sql_data(conn, cursor, n, title):
    cursor.execute('DELETE FROM ex0%s_movies WHERE title = %s;', (n, title))
    deleted_rows = cursor.rowcount
    if deleted_rows:
        context = {'status': 'OK', 'text': 'Data removed successfully!'}
    else:
        context = {'status': 'KO', 'text': f'No movie found with title "{title}"'}
    conn.commit()
    return context
