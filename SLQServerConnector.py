import pyodbc
from IDBConnector import IDBConnector
from ResultObject import ResultObject
from pandas import DataFrame


class SQLServerConnector(IDBConnector):
    def __init__(self, server: str, port: int, user: str, password: str, database: str = None):
        super().__init__(server, port, user, password, database)
        self.conn_params = {'DRIVER': '{ODBC Driver 17 for SQL Server}',
                            'SERVER': self.server,
                            'DATABASE': self.database,
                            'UID': self.user,
                            'PWD': self.password}

    def test_connection(self):
        with pyodbc.connect(**self.conn_params) as conn:
            try:
                cur = conn.cursor()
                cur.execute('SELECT 1')
                return IDBConnector.ResultObject(True, 'Connection successful')
            except Exception as e:
                return IDBConnector.ResultObject(False, 'Connection failed: ' + str(e))

    def query_to_df(self, query: str) -> ResultObject:
        pass

    def column_name_to_df(self, table_name: str) -> ResultObject:
        pass

    def insert_df(self, df: DataFrame, table_name: str) -> ResultObject:
        pass

    def truncate_table(self, table_name: str) -> ResultObject:
        pass

    def delete_data(self, table_name: str, where: str) -> ResultObject:
        pass
