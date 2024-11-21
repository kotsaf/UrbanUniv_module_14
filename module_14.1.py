import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

'''TASK 1'''
# for i in range(1, 11):
#     cursor.execute(' INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}',
#                                                                         f'example{i}@gmail.com', f'{i * 10}', '1000'))

'''TASK 2'''
# cursor.execute(' UPDATE Users SET balance = ? WHERE id % 2 > 0', (500, ))

'''TASK 3'''
# k = 1
# while k < 11:
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{k}', ))
#     k += 3

cursor.execute('SELECT * FROM Users')                  # GROUP - sorting
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()

'''RUN'''
# (2, 'User2', 'example2@gmail.com', 20, 1000)
# (3, 'User3', 'example3@gmail.com', 30, 500)
# (5, 'User5', 'example5@gmail.com', 50, 500)
# (6, 'User6', 'example6@gmail.com', 60, 1000)
# (8, 'User8', 'example8@gmail.com', 80, 1000)
# (9, 'User9', 'example9@gmail.com', 90, 500)
