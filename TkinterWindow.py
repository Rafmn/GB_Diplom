import os
from tkinter import *
from tkinter import ttk

def tkinter(list):
    root = Tk()
    root.title("Список книг")
    root.geometry("600x200")
    scrolbar = Scrollbar(root)
    scrolbar.pack( side = RIGHT, fill = Y )

    l_var = Variable(value=list)
    l_listbox = Listbox(root, listvariable=l_var, yscrollcommand = scrolbar.set)
    l_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)    
    
    root.mainloop()

def questionConvert():
    root = Tk()
    root.geometry("300x150")
    root.title("Конвертация")

    label = Label(text="Сконвентировать книгу в устройство Kindle?") 
    label.pack()  
              
    btnY = ttk.Button(text="Yes", command=convert)
    btnN = ttk.Button(text="No", command=quit)
    btnY.pack(fill=X)
    btnN.pack(fill=X)
    root.mainloop()

def convert():
    os.system("python 'DragAndDrop.py'")

