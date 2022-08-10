import mariadb
import mariadb as m

from database.queriesManager import QueriesManager as qm


class DataBaseManager:

    def __init__(self):
        self.conn = m.Connection(
            user="u6h4sir814popwrc",
            password="V9oARG43hxkx6I6ISrbf",
            host="beoi7s59mz6ilseh5hpr-mysql.services.clever-cloud.com",
            port=3306,
            database="beoi7s59mz6ilseh5hpr"
        )
        self.cursor = self.conn.cursor()

    def query(self, query: str, data: tuple) -> bool:
        self.cursor.execute(query, data)

    def queries(self, data: dict) -> bool:
        for item in data.keys():
            try:
                self.cursor.execute(data[item]['query'], data[item]['values'])
            except mariadb.DataError:
                print(data[item]['values'])
        self.conn.commit()

    def executeQueriesByDict(self, *args):
        data = qm.createInfoForQueries(args[1], args[0])
        self.queries(data)
