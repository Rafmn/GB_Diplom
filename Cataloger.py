import os
import fnmatch
from bs4 import BeautifulSoup

from TkinterWindow import tkinter

# Получение списка файлов в папке Books и сохранение их в list_of_files
list_of_files = []
listOfFiles = os.listdir("./Books")
# listOfFiles1 = os.listdir("/home/marat/Library")
pattern = "*.fb2"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        list_of_files.append(entry)
# for entry in listOfFiles1:
#     if fnmatch.fnmatch(entry, pattern):
#         list_of_files.append(entry)

# Извлечение данных из файла
def get_fb2_info(fname, tag):
    with open(fname, 'r', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'xml')
    if soup.find(tag, {'value': True}):
        return soup.find(tag, {'value': True})['value']
    elif soup.find(tag):
        return soup.find(tag).text
    
# Вывод списка в консоль
myList = []
for i in range(len(list_of_files)):
    author_f = get_fb2_info(f'./Books/{list_of_files[i]}', 'author').replace("\n", " ")
    book_title_f = get_fb2_info(f'./Books/{list_of_files[i]}', 'book-title').replace("\n", " ")
    s = str(i+1) + '. ' + '"' + book_title_f + '"' + ',' + ' ' + author_f
    myList.append(s)

# Отправление списка в окно Tkinter
tkinter(myList)