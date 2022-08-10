from tkinter import *

from elements.custonTextArea import CustomTextArea


class WindowsText(Tk):

    def __init__(self, txt: str, title: str = 'Informacion'):
        super().__init__()
        self.geometry("500x350")
        self.title(title)
        self.frame = Frame(self)
        self.frame.config(bg="pink")
        self.frame.pack(expand=True, fill=BOTH)
        self.area = CustomTextArea(self.frame)
        self.area.setText(txt)
