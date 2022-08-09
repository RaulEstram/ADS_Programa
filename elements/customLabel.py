import tkinter as tk


class CustomLabel(tk.Label):

    def __init__(self, master, txt):
        super().__init__(master, text=txt)
        self._master = master
        self.config(
            bg="white",
            font=("JetBrains Mono", 12),
            anchor="e",
        )
