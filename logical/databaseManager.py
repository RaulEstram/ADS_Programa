import mariadb as m


class DataBaseManager:

    def __init__(self):
        try:
            self.conn = m.Connection(
                user="u6h4sir814popwrc",
                password="V9oARG43hxkx6I6ISrbf",
                host="beoi7s59mz6ilseh5hpr-mysql.services.clever-cloud.com",
                port=3306,
                database="beoi7s59mz6ilseh5hpr"
            )
            self.cursor = self.conn.cursor()
        except m.Error as e:
            print(e)

    def query(self, query: str, data: tuple) -> bool:
        self.cursor.execute(query, data)

    def queries(self, data: dict) -> bool:
        #TODO: crear funcion que realice varios execute
        pass
