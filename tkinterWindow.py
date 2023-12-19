'''Окно взаимодействия с пользователем'''

import os
import subprocess
from tkinter import *
from tkinter import ttk
import fnmatch


from fb2_info import Fb2_info
from db import DB
from private_data import path_to_folder_books

PATH_BOOKS = path_to_folder_books


def tkinter(a_list, list_of_files_urls):
    root = Tk()
    root.title("Список книг")
    root.geometry("700x500")

    def convert():
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            num = item["values"][0]
            a_path = list_of_files_urls[num-1]

        print(a_path)
        subprocess.call(['./fb2c_linux_amd64/fb2c', '-c', './fb2c_linux_amd64/configuration.toml',
                         'convert', '--to', 'azw3', a_path,
                         '/run/media/marat/Kindle/documents'], text=True)
        subprocess.call(['./fb2c_linux_amd64/fb2c', 'synccovers',
                         '/run/media/marat/Kindle/documents'])
        print("Successfully")

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            num = item["values"][0]
            a_path = list_of_files_urls[num-1]
            v.set(Fb2_info().get_info_by_meta(a_path, 'description'))

    def search_book():
        text = entry.get()
        list1 = DB().search_title_book(text)
        list_books = [(i[1].split(), i[2])
                      for _, i in enumerate(list1)]
        v.set(list_books)

    def sync():
        list_of_files = os.listdir(PATH_BOOKS)
        pattern = "*.fb2"
        for entry in list_of_files:
            absolute_path_file = os.path.abspath(path_to_folder_books + entry)
            if fnmatch.fnmatch(entry, pattern):
                if not DB().search_name_file(entry):
                    # Если книги нет в базе, то добавляем ее туда:
                    try:
                        author = Fb2_info().get_fb2_info(absolute_path_file, 'author')
                        book_title = Fb2_info().get_fb2_info(absolute_path_file, 'book-title')
                        DB(author, book_title, entry,
                           absolute_path_file).add_book()
                    except UnicodeDecodeError:
                        print(entry, "Не добавлен")
        v.set("Синхронизировано")

    frame1 = Frame(root)
    conv_bt = Button(frame1, text="Конвертировать", command=convert)
    sync_bt = Button(frame1, text="Синхронизировать", command=sync)
    conv_bt.pack(side=LEFT)
    sync_bt.pack(side=RIGHT)
    frame1.pack()

    for c in range(2):
        root.columnconfigure(index=c, weight=1)
    for r in range(2):
        root.rowconfigure(index=r, weight=1)

    frame2 = Frame(root)
    entry = ttk.Entry(frame2)
    entry.pack(side=LEFT)
    btn = ttk.Button(frame2, text="Искать", command=search_book)
    btn.pack(side=LEFT)
    frame2.pack()

    colums = ("number", "name", "title")
    tree = ttk.Treeview(columns=colums, show='headings')
    tree.pack(fill=BOTH, expand=1)
    tree.column("#1", stretch=NO, width=50)
    tree.column("#2", stretch=NO, width=170)

    scrolbar = Scrollbar(tree)
    scrolbar.pack(side=RIGHT, fill=Y)

    tree.heading('number', text='№')
    tree.heading('name', text='Автор')
    tree.heading('title', text='Наименование')

    list_books = [(count+1, i[1].split(), i[2])
                  for count, i in enumerate(a_list)]
    for book in list_books:
        tree.insert("", END, values=book)

    tree.bind("<<TreeviewSelect>>", item_selected)

    frame3 = Frame(root)
    v = StringVar()
    mm = Label(frame3, textvariable=v, wraplength=570)
    mm.pack(anchor=NW, fill=X, padx=5, pady=5)
    frame3.pack()

    root.mainloop()


if __name__ == ('__main__'):
    tkinter([['1', 'Marat', '/home/marat/GeekBrains/Diplom/Books/chelovek-mashina(1).fb2',
              'chelovek-mashina(1).fb2'],
             ['2', 'Petya',
              '/home/marat/GeekBrains/Diplom/Books/Dauti_Sest-li-menya-moya-koshka-I-drugie-zhivotrepeshchushchie-voprosy-o-smerti.zrv9Hg.659910.fb2',
              'voprosy-o-smerti.zrv9Hg.659910.fb2']],
            ['/home/marat/GeekBrains/Diplom/Books/chelovek-mashina(1).fb2',
             '/home/marat/GeekBrains/Diplom/Books/Izmienchivaia priroda matiemati - S. Krants.fb2'])
