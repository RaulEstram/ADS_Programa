import tkinter as tk

from elements.customButton import CustomButton
from elements.customEntry import CustomEntry
from elements.customLabel import CustomLabel
from elements.customTextArea import CustomTextArea
from elements.customCanva import Canva

from logical.adsRequests import ADS
from logical.files import FilesManagger

from database.databaseManager import DataBaseManager
from database.queriesManager import QueriesManager


class Search(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._master = master
        self.buscadorEntry = None
        self.buscarButton = None
        self.buscarLabel = None
        self.textArea = None
        self.botonCSV = None
        self.botonQueries = None
        self.data = {}
        self.obtenerTexto = None
        self.ads = ADS("TnEWAPDi8n5R3taijqXleJDTZ5LNDr2LMJjOOsec")
        self.config(
            bg="#fff"
        )
        self.loadWidgets()
        self.queries = QueriesManager()

    def loadWidgets(self):
        self.buscarLabel = CustomLabel(self, "Buscar:")
        self.buscarLabel.place(relx=0.09, rely=0.0005, relwidth=0.15, height=35)

        self.buscadorEntry = CustomEntry(self)
        self.buscadorEntry.place(relx=.25, rely=0.0005, relwidth=0.5, height=35)

        self.buscarButton = CustomButton(self, "Buscar",
                                         lambda: self.ads.getDataByKey(self.buscadorEntry.get(), self))
        self.buscarButton.place(relx=0.76, rely=0.0005, relwidth=0.15)

        self.textArea = CustomTextArea(self)
        self.textArea.place(relx=0.12, rely=0.002, relwidth=0.82, relheight=0.006)

        self.botonCSV = CustomButton(self, "Guardar CSV", command=lambda: FilesManagger.saveDictAsCsvFile(
            self.data))  # TODO: cambiar command
        self.botonCSV.place(rely=0.0085, relx=0.12)

        self.botonQueries = CustomButton(self, "Ver Queries", command=self.showQueries)
        self.botonQueries.place(rely=0.0085, relx=0.4)

        self.botonSave = CustomButton(self, "Guardar Informacion", command=self.saveDataInDataBase)
        self.botonSave.place(rely=0.0085, relx=0.6)

    def reloadTextArea(self, txt):
        self.textArea.destroy()
        self.textArea = CustomTextArea(self)
        self.textArea.place(relx=0.12, rely=0.002, relwidth=0.82, relheight=0.006)
        self.textArea.setText(txt)

    def showQueries(self):
        canva = Canva(
            "Estos Queries Son una Previzualizacion, puede que contengan algun tipo de error\n\n" + self.queries.createPreSqlQueries(
                self.data, "raul"))

    def saveDataInDataBase(self):
        data = QueriesManager.createInfoForQueries(self.data,
                                                   "Raul")  # TODO: mejorar para que el usuario meta su nombre
        connection = DataBaseManager()
        connection.queries(data)
        pass
