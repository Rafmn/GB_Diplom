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