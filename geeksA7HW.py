# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
# 2. В БД создать таблицу products
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров.
# 8. Добавить функцию, которая меняет количество товара по id.
# 9. Добавить функцию, которая меняет цену товара по id.
# 10. Добавить функцию, которая удаляет товар по id.
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли.
# 12. Добавить функцию, которая бы выбирала из БД товары, которые дешевле лимита по цене (например 100 сом) сомов и
# количество которых больше чем лимит остатка на складе (например 5 шт) и распечатывала бы их в консоли.
# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”,
# должны соответствовать поиску товары с названием - “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.).
# 14. Протестировать каждую написанную функцию

import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(db_name, products):
    sql = '''INSERT INTO products 
    (product_title , price , quantity)
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_quantity(db_name, products):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(db_name, products):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, products)
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(db_name, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_name):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quantity(db_name, price_limit, quantity_limit):
    sql = '''SELECT id, product_title, price FROM products WHERE price <= ? AND quantity > ?'''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_by_title(db_name ):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%мыло%' '''
    try:
        with sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, )
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

db_name = '''hw.db'''
sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection(db_name)
if my_connection is not None:
    print('Connection established')
    create_table(my_connection, sql_to_create_products_table)

#     insert_products(db_name, ('жидкое мыло', 100 , 5 ))
#     insert_products(db_name, ('Натуральное мыло ручной работы "Лаванда и ромашка"', 120, 10))
#     insert_products(db_name, ('Детское мыло с экстрактом календулы', 90, 15))
#     insert_products(db_name, ('Жидкое мыло "Антибактериальное" с ароматом лимона', 110, 20))
#     insert_products(db_name, ('Мыло-скраб "Кофе и корица"', 150, 8))
#     insert_products(db_name, ('Мыло-пена для умывания "Свежесть утра"', 130, 12))
#
#     insert_products(db_name, ('Шампунь для сухих волос "Глубокое увлажнение"', 200, 10))
#     insert_products(db_name, ('Шампунь против перхоти "Ментоловая свежесть"', 220, 6))
#     insert_products(db_name, ('Шампунь для окрашенных волос "Защита цвета"', 240, 9))
#     insert_products(db_name, ('Детский шампунь "Без слёз" с ароматом персика', 180, 20))
#     insert_products(db_name, ('Шампунь с кератином для восстановления волос', 250, 7))
#
#     insert_products(db_name, ('Пена для ванны "Релакс с лавандой"', 100, 5))
#     insert_products(db_name, ('Увлажняющая пена для бритья "Свежий бриз"', 150, 10))
#     insert_products(db_name, ('Пена для укладки волос "Объём и фиксация"', 180, 12))
#     insert_products(db_name, ('Пена для лица "Глубокое очищение"', 140, 15))
#     insert_products(db_name, ('Детская пена для купания "Весёлые пузырьки"', 130, 25))

# select_all_products(db_name)
# delete_product(db_name , 4 )
# update_quantity(db_name , (12 , 1))
# update_price(db_name , (200 , 2))
# insert_products(db_name , ('мыло' , 55 , 19))
# select_by_title(db_name)
# select_products_by_price_and_quantity(db_name, 150,5)