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
for i in range(1, 11):
    cursor.execute(' INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}',
                                                                        f'example{i}@gmail.com', f'{i * 10}', '1000'))

'''TASK 2'''
cursor.execute(' UPDATE Users SET balance = ? WHERE id % 2 > 0', (500, ))

'''TASK 3'''
k = 1
while k < 11:
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{k}', ))
    k += 3

cursor.execute('SELECT * FROM Users WHERE age != 60')
users = cursor.fetchall()
for i in users:
    print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

connection.commit()
connection.close()

'''RUN'''
# Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
# Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
# Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
# Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
# Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
