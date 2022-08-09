import tkinter as tk
from tkinter import ttk
from tkinter import *


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
        self.textArea.place(x=0, y=0, relwidth=0.95, relheight=0.95)
        self.scrollX.config(command=self.textArea.xview)
        self.scrollY.config(command=self.textArea.yview)
        pass

    def createScrolls(self):
        self.scrollY = Scrollbar(self)
        self.scrollY.place(relx=0.95, y=0, relheight=0.95)

        self.scrollX = Scrollbar(self, orient=tk.HORIZONTAL)
        self.scrollX.place(x=0, rely=0.95, relwidth=0.95)

    def setText(self, txt):
        self.textArea.insert(tk.INSERT, txt)
