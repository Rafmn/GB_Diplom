'''Окно взаимодействия с пользователем'''

import os
import subprocess
from tkinter import *
from tkinter import ttk

from fb2_info import Fb2_info


def tkinter(list, list_of_files_urls):
    root = Tk()
    root.title("Список книг")
    root.geometry("600x500")
    scrolbar = Scrollbar(root)
    scrolbar.pack( side = RIGHT, fill = Y )


    def convert():
        index = l_listbox.curselection()[0]
        a_path = list_of_files_urls[index]

        print(a_path)
        subprocess.call(['./fb2c_linux_amd64/fb2c', '-c', './fb2c_linux_amd64/configuration.toml',\
                          'convert', '--to', 'azw3', a_path,\
                              '/run/media/marat/Kindle/documents'], text = True)
        subprocess.call(['./fb2c_linux_amd64/fb2c', 'synccovers',\
                          '/run/media/marat/Kindle/documents'])
        print("Successfully")

    def show_description():
        index = l_listbox.curselection()[0]
        a_path = list_of_files_urls[index]
        v.set(Fb2_info().get_info_by_meta(a_path, 'description'))

    Button(root, text="Конвертировать", command = convert).pack(fill=X)
    Button(root, text='Описание', command=show_description).pack(fill=X)

    list = [(i[1], i[2]) for i in list]
    l_var = Variable(value=list)
    l_listbox = Listbox(root, listvariable=l_var, yscrollcommand = scrolbar.set)
    l_listbox.pack(anchor=N, fill=X, padx=5, pady=5)

    v = StringVar()
    mm = Label(root, textvariable=v, wraplength=500)
    mm.pack(anchor=NW, fill=X, padx=5, pady=5)

    root.mainloop()

if __name__ == ('__main__'):
    tkinter([['1', 'Marat', '/home/marat/GeekBrains/Diplom/Books/chelovek-mashina(1).fb2', 'chelovek-mashina(1).fb2'], ['2', 'Petya', '/home/marat/GeekBrains/Diplom/Books/Dauti_Sest-li-menya-moya-koshka-I-drugie-zhivotrepeshchushchie-voprosy-o-smerti.zrv9Hg.659910.fb2', 'voprosy-o-smerti.zrv9Hg.659910.fb2']], ['/home/marat/GeekBrains/Diplom/Books/chelovek-mashina(1).fb2', '/home/marat/GeekBrains/Diplom/Books/Izmienchivaia priroda matiemati - S. Krants.fb2'])