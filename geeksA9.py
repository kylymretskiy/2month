import sqlite3

def create_connection(db_name):
    """Создаёт подключение к базе данных SQLite"""
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except sqlite3.Error as e:
        print(f"Ошибка подключения: {e}")
        return None

def create_table(connection, create_table_sql):
    """Создаёт таблицу в базе данных"""
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при создании таблицы: {e}")

def insert_product(connection, product):
    """Вставляет продукт в таблицу products"""
    sql = '''
    INSERT INTO products (title, category_code, unit_price, stock_quantity, store_id)
    VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении продукта: {e}")

def insert_category(connection, category):
    """Вставляет категорию в таблицу categories"""
    sql = '''
    INSERT INTO categories (title, code)
    VALUES (?, ?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, category)
        connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении категории: {e}")

def insert_store(connection, store):
    """Вставляет магазин в таблицу stores"""
    sql = '''
    INSERT INTO stores (title)
    VALUES (?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (store,))
        connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при добавлении магазина: {e}")

# Создаём соединение
db_name = "store.db"
connection = create_connection(db_name)

# SQL-запросы для создания таблиц
sql_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category_code TEXT NOT NULL,
    unit_price REAL DEFAULT 0.0,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories (code),
    FOREIGN KEY (store_id) REFERENCES stores (id)
)
'''

sql_create_categories_table = '''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    code TEXT NOT NULL UNIQUE
)
'''

sql_create_stores_table = '''
CREATE TABLE IF NOT EXISTS stores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
'''

# Создаём таблицы
if connection:
    create_table(connection, sql_create_products_table)
    create_table(connection, sql_create_categories_table)
    create_table(connection, sql_create_stores_table)
    print("Таблицы успешно созданы!")

    # Добавляем категории
    categories = [("Food products", "FD"), ("Electronics", "EL"), ("Clothes", "CL")]
    for category in categories:
        insert_category(connection, category)

    # Добавляем магазины
    insert_store(connection, "Asia")
    insert_store(connection, "Globus")
    insert_store(connection, "Spar")

    # Добавляем продукты
    insert_product(connection, ("Chocolate", "FD", 10.5, 129, 1))
    insert_product(connection, ("MacBook", "EL", 800, 10, 2))
    insert_product(connection, ("T-Shirt", "CL", 0.0, 15, 1))

    connection.close()
    print("Соединение закрыто.")
else:
    print("Ошибка: соединение не установлено!")


