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
        self.responsive()

    def loadWidgets(self):
        self.buscarLabel = CustomLabel(self, "Buscar:")
        self.buscarLabel.grid(row=1, column=1, sticky="nsew")  # TODO: cambiar posicion

        self.buscadorEntry = CustomEntry(self)
        self.buscadorEntry.grid(row=1, column=2, columnspan=5, sticky="nsew")  # TODO: cambiar posicion

        self.buscarButton = CustomButton(self, "Buscar",
                                         lambda: self.ads.getDataByKey(self.buscadorEntry.get(), self))
        self.buscarButton.grid(row=1, column=8, sticky="nsew")  # TODO: cambiar posicion

        self.textArea = tk.Frame(self)
        self.textArea.grid(row=3, rowspan=14, column=1, columnspan=8, sticky="nsew")  # TODO: cambiar posicion

        self.botonCSV = CustomButton(self, "Guardar CSV", command=lambda: FilesManagger.saveDictAsCsvFile(
            self.data))  # TODO: cambiar command
        self.botonCSV.grid(row=18, column=1, sticky="nsew")  # TODO: cambiar posicion

        self.botonQueries = CustomButton(self, "Ver Queries", command=self.showQueries)
        self.botonQueries.grid(row=18, column=2, sticky="nsew")  # TODO: cambiar posicion

        self.botonSave = CustomButton(self, "Guardar Informacion", command=self.saveDataInDataBase)
        self.botonSave.grid(row=18, column=3, sticky="nsew")  # TODO: cambiar posicion

    def responsive(self):
        row = 20
        columns = 10
        for i in range(row):
            self.rowconfigure(i, weight=1)
        for i in range(columns):
            self.columnconfigure(i, weight=1)

    def reloadTextArea(self, txt):
        self.textArea.destroy()
        self.textArea = CustomTextArea(self)
        self.textArea.grid(row=0, column=0, sticky="nsew")  # TODO: cambiar posicion
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
