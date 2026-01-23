def update_sql_data(conn, cursor, n, title, opening_crawl):
    cursor.execute('UPDATE ex0%s_movies SET opening_crawl = %s WHERE title = %s;', (n, opening_crawl, title))
    updated_rows = cursor.rowcount
    if updated_rows:
        context = {'status': 'OK', 'text': 'Data updated successfully!'}
    else:
        context = {'status': 'KO', 'text': f'No movie found with title "{title}"'}
    conn.commit()
    return context
