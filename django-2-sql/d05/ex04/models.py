def remove_sql_data(conn, cursor, n, title):
    cursor.execute('DELETE FROM ex0%s_movies WHERE title = %s;', (n, title))
    deleted_rows = cursor.rowcount
    if deleted_rows:
        context = {'status': 'OK', 'text': 'Data removed successfully!'}
    else:
        context = {'status': 'KO', 'text': 'No data found to remove!'}
    conn.commit()
    return context
