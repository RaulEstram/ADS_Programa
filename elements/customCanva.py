from tkinter import *

from elements.customTextArea import CustomTextArea


class Canva(Tk):

    def __init__(self, txt: str):
        super().__init__()
        self.geometry("500x350")
        self.text = CustomTextArea(self)
        self.text.pack(expand=True, fill=BOTH)
        self.text.setText(txt)
