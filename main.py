from tkinter import *
from interfaces.masterFrame import MasterFrame

# Creamos una ventana
root = Tk()
root.geometry("850x500")
root.title("Busqueda de Datos ADS")

# Creamos un MasterFrame que tendra todos los widgets de nuestra app
masterFrom = MasterFrame(root)

if __name__ == "__main__":
    masterFrom.mainloop()
