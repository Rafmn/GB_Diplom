import os
import fnmatch
from tkinterWindow import tkinter

from db import DB
from fb2_info import Fb2_info


# Получение списка файлов в папке Books
listOfFiles = os.listdir("./Books")
PATTERN = "*.fb2"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, PATTERN):
        absolute_path_file = os.path.abspath("./Books/" + entry)
        if not DB().search_name_file(entry):
            # Если книги нет в базе, то добавляем ее туда:
            author = Fb2_info().get_fb2_info(absolute_path_file, 'author')
            book_title = Fb2_info().get_fb2_info(absolute_path_file, 'book-title')
            DB(author, book_title, entry, absolute_path_file).add_book()


myList = DB().get_list_books() # Получение всей таблицы из базы данных MySQL
list_of_files_urls = [i[4] for i in myList]

tkinter(myList, list_of_files_urls)
