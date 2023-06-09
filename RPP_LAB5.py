import sqlite3 as db


# Создание соединения с базой данных с именем "users" (если базы данных не существует, то она будет создана)
conn = db.connect('users.db')
# Создание объекта-курсора, который используется для выполнения запросов к базе данных
cursor = conn.cursor()
# Выполнить запрос на создание таблицы пользователей, если таблица не существует
cursor.execute(''' CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
# Фиксация изменений (запись новых данных) в базе данных
conn.commit()

# Определение функции "insert", которая используется для добавления нового пользователя в базу данных
def insert(id, name, email):
    # Создание объекта-курсора
    cursor = conn.cursor()
    # Выполнить запрос на добавление нового пользователя в базу данных
    cursor.execute("""INSERT INTO users(id, name, email) VALUES (:id, :name, :email)""",
              {"id": id, "name": name, "email": email})
    # Фиксация изменений (запись новых данных) в базе данных
    conn.commit()

def select_ex(name, email):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM users WHERE name=:name AND email=:email""",
                   {"name": name, "email": email})
    print(cursor.fetchall())



# Определение функции "select", которая используется для выбора всех пользователей из базы данных
def select():
    # Создание объекта-курсора
    cursor = conn.cursor()
    # Выполнение запроса на выбор всех пользователей из таблицы "users"
    cursor.execute("""SELECT * FROM users""")
    # Печать всех выбранных данных
    print(cursor.fetchall())

# Определение функции "select_user", которая используется для выбора информации о пользователе по его ID
def select_user(id):
    # Создание объекта-курсора
    cursor = conn.cursor()
    # Выполнение запроса на выбор пользователя с заданным ID
    cursor.execute("""SELECT * FROM users WHERE id=:id""", {"id": id})
    # Печать информации о выбранном пользователе
    print(cursor.fetchall())

# Определение функции "delete_user", которая используется для удаления пользователя по его ID
def delete_user(id):
    # Создание объекта-курсора
    cursor = conn.cursor()
    # Выполнение запроса на удаление пользователя с заданным ID
    cursor.execute("""DELETE FROM users WHERE id=:id""", {"id": id})
    # Фиксация изменений (запись новых данных) в базе данных
    conn.commit()

# Определение функции "main", которая содержит вызовы функций для добавления пользователей в базу данных, вывода информации о них и удаления пользователя
def main():
    # Добавление двух пользователей в базу данных
    #insert(1, 'User1', 'User1@icloud.com')
    #insert(2, 'User2', 'User2@icloud.com')
    # Вывод всех пользователей из базы данных
    #select()
    # Вывод информации о пользователе с ID=1
    #select_user(1)
    select_ex( "User1", "User1@icloud.com")
    # Удаление пользователя с ID=2
    #delete_user(2)
    # Вывод всех пользователей из базы данных
    #select()

# Вызов функции "main"
main()
# Закрытие соединения с базой данных
conn.close()





