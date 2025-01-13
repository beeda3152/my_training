import sqlite3

def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    discription TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        for i in range(1,5):
            cursor.execute("INSERT INTO Products (title, discription, price) VALUES (?, ?, ?)", (f'Продукт {i}', f'Oписание {i}', f'{i * 100}'))

    connection.commit()
    connection.close()

    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    connection.close()
    return prod

def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)",
                   (username, email, age))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM Users WHERE USERNAME=?", (username, ))
    bl = cursor.fetchone()
    connection.close()
    return bl is not None

