import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    users = cursor.fetchall()
    for i in users:
        print(i)

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)', (f'{username}', f'{email}', f'{age}', f'1000'))
    connection.commit()

def is_included(username):
    checking = cursor.execute('SELECT * FROM Users WHERE username = ?', (f'{username}', )).fetchone()
    if checking is None:
        return False
    return True




