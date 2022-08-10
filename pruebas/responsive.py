from tkinter import *

import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("750x500")
root.title("Responsive")

# Creamos un MasterFrame que tendra todos los widgets de nuestra app
root = Frame(root)
root.config(bg="pink")
root.pack(expand=True, fill=tk.BOTH)

scrollY = Scrollbar(root)
scrollX = Scrollbar(root, orient=tk.HORIZONTAL)
area = Text(root, wrap=NONE, xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)

scrollX.config(command=area.xview)
scrollY.config(command=area.yview)

area.grid(column=0, row=0, sticky="nswe")
scrollX.grid(column=0, row=1, sticky="nsew")
scrollY.grid(column=1, row=0, sticky="nsew")

root.rowconfigure(0, weight=1000)
root.columnconfigure(0, weight=1000)
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

if __name__ == "__main__":
    root.mainloop()


class CustomTextArea(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.scrollX = None
        self.scrollY = None
        self.textArea = None
        self.config(bg="#fff")
        self.createTextArea()

    def createTextArea(self):
        self.createScrolls()
        self.textArea = Text(self, wrap=NONE, xscrollcommand=self.scrollX.set, yscrollcommand=self.scrollY.set)
        self.textArea.grid(column=0, row=0, sticky="nsew")
        self.scrollX.config(command=self.textArea.xview)
        self.scrollY.config(command=self.textArea.yview)
        pass

    def createScrolls(self):
        self.scrollY = Scrollbar(self)
        self.scrollY.grid(column=1, row=0, sticky="nsew")

        self.scrollX = Scrollbar(self, orient=tk.HORIZONTAL)
        self.scrollX.grid(column=0, row=1, sticky="nsew")

    def responsive(self):
        for i in range(2):
            self.rowconfigure(i, weight=1)
        for i in range(2):
            self.columnconfigure(i, weight=1)

    def setText(self, txt):
        self.textArea.insert(tk.INSERT, txt)
