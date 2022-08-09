import tkinter as tk


class CustomEntry(tk.Entry):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.config(
            bg="white",
            font=("JetBrains Mono", 10),
            relief=tk.SOLID,
            borderwidth=1,
            highlightcolor="pink",
            justify=tk.LEFT,
            selectbackground="#1a1a1a",
            selectborderwidth=0,
            selectforeground="#fff",
        )
