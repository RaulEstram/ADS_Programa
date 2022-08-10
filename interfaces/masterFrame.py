import tkinter as tk
from tkinter import *

from interfaces.menu import BarMenu


class MasterFrame(tk.Frame):
    focusWidget = None

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.barMenu = None
        self.title = None
        self.titleFrame = None
        self.config(
            bg="pink",
            relief=tk.FLAT,
            width=700,
            height=450
        )  # TODO: cambiar color
        self.pack(expand=True, fill=tk.BOTH)
        self.createBarMenu()
        self.createTitle()
        self.responsive()

    def createBarMenu(self):
        self.barMenu = BarMenu(self, self.createFrame)
        self.barMenu.grid(column=0, row=1, sticky="nsew")  # TODO: Grid

    def createTitle(self):
        self.titleFrame = Frame(self)
        self.titleFrame.config(bg="#1a1a1a")
        self.titleFrame.grid(column=1, row=0, sticky="nsew")  # TODO: Grid

        self.title = Label(self.titleFrame)
        self.title.config(text="Menu", fg="#bfbfbf", bg='#1a1a1a', font=("JetBrains Mono", 25))
        self.title.pack(fill=tk.BOTH, expand=True)

    def createFrame(self, widget, title):
        if self.focusWidget is not None:
            self.deleteFrame()
        self.focusWidget = widget(self)
        self.focusWidget.grid(row=1, column=1, sticky="nsew")  # TODO: Grid
        self.title.config(text=title)

    def deleteFrame(self):
        self.focusWidget.destroy()

    def responsive(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=5)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=12)
        pass
