from database import get_db_connection

def get_books(id=None, bookId=None, title=None, author=None, published_date=None, quantity=None):
    query = 'SELECT * FROM books WHERE 1=1'
    params = []

    if id:
        query += ' AND id = ?'
        params.append(id)
    if bookId:
        query += ' AND bookId = ?'
        params.append(bookId)
    if title:
        query += ' AND title LIKE ?'
        params.append(f"%{title}%")  
    if author:
        query += ' AND author LIKE ?'
        params.append(f"%{author}%")
    if published_date:
        query += ' AND published_date = ?'
        params.append(published_date)
    if quantity is not None:
        query += ' AND quantity = ?'
        params.append(quantity)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    books = cursor.fetchall()
    conn.close()

    return books



def add_book(bookId,title, author, published_date, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (bookId,title, author, published_date, quantity)
        VALUES (?, ?, ?, ?, ?)
    ''', (bookId,title, author, published_date, quantity))
    conn.commit()
    conn.close()


def update_book(id=None, bookId=None, title=None, author=None, published_date=None, quantity=None,
                new_id=None, new_bookId=None, new_title=None, new_author=None, new_published_date=None, new_quantity=None):
    query = 'UPDATE books SET'
    params = []

    # Update the fields only if new values are provided
    if new_title:
        query += ' title = ?,'
        params.append(new_title)
    if new_author:
        query += ' author = ?,'
        params.append(new_author)
    if new_published_date:
        query += ' published_date = ?,'
        params.append(new_published_date)
    if new_quantity is not None:  # quantity can be 0, so check if it's explicitly passed
        query += ' quantity = ?,'
        params.append(new_quantity)
    if new_bookId:
        query += ' bookId = ?,'
        params.append(new_bookId)
    if new_id:
        query += ' id = ?,'
        params.append(new_id)

    # Remove trailing comma
    query = query.rstrip(',')

    # Add the WHERE condition to update the right book(s)
    conditions = []
    if id:
        conditions.append('id = ?')
        params.append(id)
    if bookId:
        conditions.append('bookId = ?')
        params.append(bookId)
    if title:
        conditions.append('title LIKE ?')
        params.append(f'%{title}%')
    if author:
        conditions.append('author LIKE ?')
        params.append(f'%{author}%')
    if published_date:
        conditions.append('published_date = ?')
        params.append(published_date)
    if quantity is not None:  # quantity can be 0, so check if it's explicitly passed
        conditions.append('quantity = ?')
        params.append(quantity)

    if conditions:
        query += ' WHERE ' + ' AND '.join(conditions)

    # Execute the query
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, tuple(params))
    conn.commit()

    # Return True if at least one row was affected
    if cursor.rowcount > 0:
        conn.close()
        return True
    else:
        conn.close()
        return False



def delete_book(id=None, bookId=None, title=None, author=None, published_date=None, quantity=None):
    # Initialize the query and parameters list
    query = 'DELETE FROM books WHERE 1=1'
    params = []

    # Add conditions based on the parameters provided
    if id:
        query += ' AND id = ?'
        params.append(id)
    if bookId:
        query += ' AND bookId = ?'
        params.append(bookId)
    if title:
        query += ' AND title = ?'
        params.append(title)
    if author:
        query += ' AND author = ?'
        params.append(author)
    if published_date:
        query += ' AND published_date = ?'
        params.append(published_date)
    if quantity is not None:  # quantity can be 0, so check if it's explicitly passed
        query += ' AND quantity = ?'
        params.append(quantity)

    conn = get_db_connection()
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query, tuple(params))

    conn.commit()

    # Check if any row was deleted
    if cursor.rowcount > 0:
        conn.close()
        return True
    else:
        conn.close()
        return False
