import mysql.connector

import private_data

DB_NAME = private_data.base
PASSWORD = private_data.password
HOST_NAME = private_data.host
USER = private_data.user
PORT = private_data.port


class DB():
    """Работа с базой данных MySQL"""
    def __init__(self, author=None, book=None, namefile=None, file=None):
        self.author = author
        self.book = book
        self.namefile = namefile
        self.file = file

    def connect_db(self):
        """Подключение к базе"""
        cnx = mysql.connector.connect(user=USER,
                                      password=PASSWORD,
                                      host=HOST_NAME,
                                      port=PORT)

        cursor = cnx.cursor()

        try:
            # Попытка создания базы:
            create_db_query = "CREATE DATABASE Diplom_DB"
            cursor.execute(create_db_query)
            #  Подключаемся:
            cursor.close()
            cnx.close()
            cnx = mysql.connector.connect(user=USER,
                                          password=PASSWORD,
                                          host=HOST_NAME,
                                          port=PORT,
                                          database=DB_NAME)

            # Создаем таблицы:
            cursor = cnx.cursor()

            create_books_table_query = """
                CREATE TABLE books(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    author VARCHAR(100),
                    book_title VARCHAR(100),
                    file_name VARCHAR(100),
                    url_file VARCHAR(200)
                )
                """
            # with cursor:
            cursor.execute(create_books_table_query)
            cnx.commit()

        except mysql.connector.Error as e:
            # Если база существует, переподключаемся к ней:
            cursor.close()
            cnx.close()
            cnx = mysql.connector.connect(user=USER,
                                          password=PASSWORD,
                                          host=HOST_NAME,
                                          port=PORT,
                                          database=DB_NAME)
            print(e)

        # cursor.close()
        # cnx.close()
        cursor = cnx.cursor()
        return cursor, cnx

    def add_book(self):
        """Добавление книги в базу"""
        cursor, cnx = DB.connect_db(self)
        insert_book_quety = """
            INSERT INTO books (author, book_title, file_name, url_file) 
            VALUES ( %s, %s, %s, %s)"""
        book_record = [(self.author, self.book, self.namefile, self.file),]
        cursor.executemany(insert_book_quety, book_record)
        cnx.commit()
        cursor.close()
        cnx.close()

    def search_name_file(self, nfile: str):
        """поиск файла в базе MySQL"""
        cursor, cnx = DB.connect_db(self)
        search_name_file = """SELECT * FROM books WHERE file_name LIKE %s"""
        book_name = [(nfile),]
        cursor.execute(search_name_file, book_name)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return bool(result)

    def get_list_books(self):
        """Получение таблицы из базы"""
        cursor, cnx = DB.connect_db(self)
        list_of_files = []
        try:
            cursor.execute("SELECT * FROM books")
            result = cursor.fetchall()
            for x in result:
                list_of_files.append(x)
        except OSError:
            cnx.rollback()

        cursor.close()
        cnx.close()

        return list_of_files
