import tkinter as tk
from elements.customButton import CustomButton
from interfaces.home import Home
from interfaces.search import Search


class BarMenu(tk.Frame):

    def __init__(self, master, command):
        super().__init__(master)
        self._master = master
        self._command = command
        self.config(
            bg="#1a1a1a",
        )
        self.createButtons()

    def createButtons(self):

        homeButton = CustomButton(self, "Home", lambda: self._command(Home, "Home"))
        homeButton.place(rely=0.15, x=0, relwidth=1, relheight=0.1)

        searchButton = CustomButton(self, "Buscar", lambda: self._command(Search, "Buscar"))
        searchButton.place(rely=0.25, x=0, relwidth=1, relheight=0.1)
