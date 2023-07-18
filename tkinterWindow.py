'''Окно взаимодействия с пользователем'''

import os
import subprocess
from tkinter import *
# from tkinter import ttk
# from tkinter import Menu  

def tkinter(list, list_of_files):
    root = Tk()
    root.title("Список книг")
    root.geometry("600x200")
    scrolbar = Scrollbar(root)
    scrolbar.pack( side = RIGHT, fill = Y )

    def convert():
        index = l_listbox.curselection()[0]
        a_path = os.path.join('./Books', list_of_files[index])
        print(a_path)
        subprocess.call(['./fb2c_linux_amd64/fb2c', '-c', './fb2c_linux_amd64/configuration.toml',\
                          'convert', '--to', 'azw3', a_path,\
                              '/run/media/marat/Kindle/documents'], text = True)
        subprocess.call(['./fb2c_linux_amd64/fb2c', 'synccovers',\
                          '/run/media/marat/Kindle/documents'])
        # os.system("python 'DragAndDrop.py'")
        print("Successfully")

    Button(root, text="Конвертировать", command = convert).pack(fill=X)

    l_var = Variable(value=list)
    l_listbox = Listbox(root, listvariable=l_var, yscrollcommand = scrolbar.set)
    l_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)   

    root.mainloop()

