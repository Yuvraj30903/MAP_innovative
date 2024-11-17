import sqlite3

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bookId INTEGER NOT NULL,
            title TEXT NOT NULL, 
            author TEXT NOT NULL,
            published_date TEXT,
            quantity INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
