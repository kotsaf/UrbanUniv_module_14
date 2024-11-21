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

for i in range(1, 11):
    cursor.execute(' INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}',
                                                                        f'example{i}@gmail.com', f'{i * 10}', '1000'))

cursor.execute(' UPDATE Users SET balance = ? WHERE id % 2 > 0', (500, ))

k = 1
while k < 11:
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{k}', ))
    k += 3

cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
balance_sum = cursor.fetchone()[0]

print(f'Средний баланс пользователя: {balance_sum / total}')

connection.commit()
connection.close()
