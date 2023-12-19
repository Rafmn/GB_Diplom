import subprocess
from tkinter import filedialog

def drop(event):
    global path_file
    path_file = event.data
    lb.insert(tk.END, path_file)

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Frame, Button, Style

from tkinterdnd2 import DND_FILES, TkinterDnD


root1 = TkinterDnD.Tk()  # notice - use this instead of tk.Tk()
root1.title("Прием *fb2")


lb = tk.Listbox(root1)
lb.insert(1, "Переместите сюда *fb2")

lb.drop_target_register(DND_FILES)
lb.dnd_bind('<<Drop>>', drop)
quitButton = ttk.Button(text="Конвентировать", command=root1.destroy)
lb.pack()
quitButton.pack()
root1.mainloop()

subprocess.call(['./fb2c_linux_amd64/fb2c', '-c', './fb2c_linux_amd64/configuration.toml', 'convert', '--to', 'azw3', path_file, '/run/media/marat/Kindle/documents'])
subprocess.call(['./fb2c_linux_amd64/fb2c', 'synccovers', '/run/media/marat/Kindle/documents'])

print("Successfully")

