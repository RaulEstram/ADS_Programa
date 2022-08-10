from tkinter import messagebox
import mariadb as m

from database.queriesManager import QueriesManager as qm


class DataBaseManager:

    def __init__(self):
        self._conn = None
        self._cursor = None
        self._status = False
        try:
            self._conn = m.Connection(
                user="u6h4sir814popwrc",
                password="V9oARG43hxkx6I6ISrbf",
                host="beoi7s59mz6ilseh5hpr-mysql.services.clever-cloud.com",
                port=3306,
                database="beoi7s59mz6ilseh5hpr"
            )
            self._cursor = self._conn.cursor()
            self._status = True
        except m.OperationalError:
            messagebox.showerror("Error en la conexcion a la DB",
                                 "Se produjo un Error al intentar conectarse a la base de datos")

    def getStatus(self):
        return self._status

    def query(self, query: str, data: tuple) -> bool:
        self._cursor.execute(query, data)
        return True

    def queries(self, data: dict) -> bool:
        for item in data.keys():
            try:
                self._cursor.execute(data[item]['query'], data[item]['values'])
                self._conn.commit()
            except m.DataError:
                print(data[item]['values'])
        self._conn.commit()
        return True

    def executeQueriesByDict(self, *args):
        data = qm.createInfoForQueries(args[1], args[0])
        self.queries(data)
