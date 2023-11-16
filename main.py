from tkinterWindow import tkinter

from db import DB


myList = DB().get_list_books()  # Получение всей таблицы из базы данных MySQL
list_of_files_urls = tuple([i[4] for i in myList])

tkinter(myList, list_of_files_urls)
