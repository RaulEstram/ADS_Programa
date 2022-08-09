from tkinter import *
import tkinter as tk


class Home(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.config(
            bg="purple"
        )
        self.loadWidgets()

    def loadWidgets(self):
        titulo = Label(self)
        titulo.config(text="hola mundo")
        titulo.place(x=0, y=0, relheight=0.001, relwidth=1)
