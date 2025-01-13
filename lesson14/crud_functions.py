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

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products')
    prod = cursor.fetchall()
    connection.close()
    return prod