from IDBConnector import IDBConnector
import mysql.connector
from ResultObject import ResultObject
import pandas as pd


class MySqlConnector(IDBConnector):
    def __init__(self, server: str, port: int, user: str, password: str, database: str = None):
        super().__init__(server, port, user, password, database)
        self.conn_params = {'host': self.server,
                            'port': self.port,
                            'user': self.user,
                            'password': self.password,
                            'database': self.database}

    def test_connection(self):
        try:
            with mysql.connector.connect(**self.conn_params) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT 1')
                myresult = cursor.fetchall()
                if myresult[0][0] != 1:
                    return ResultObject(False, 'Unexpected value returned')
                else:
                    return ResultObject(True, 'Connection successful', myresult[0][0])
        except Exception as e:
            return ResultObject(False, 'Connection failed: ' + str(e))

    def query_to_df(self, query: str):
        try:
            with mysql.connector.connect(**self.conn_params) as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]
                result = cursor.fetchall()
                result_df = pd.DataFrame(result, columns=columns)

                return ResultObject(True, '', result_df)
        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))

    def column_name_to_df(self, table_name: str):
        try:
            with mysql.connector.connect(**self.conn_params) as conn:
                cursor = conn.cursor()
                query = f"SELECT * FROM {table_name}"
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]
                result = cursor.fetchall()
                result_df = pd.DataFrame(result, columns=columns)

                return ResultObject(True, '', result_df)
        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))

    def insert_df(self, df, table_name: str):
        pass

    def truncate_table(self, table_name: str):
        try:
            with mysql.connector.connect(**self.conn_params) as conn:
                cursor = conn.cursor()
                query = f"TRUNCATE TABLE {table_name}"
                cursor.execute(query)

                return ResultObject(True, f'{table_name} truncated',)
        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))

    def delete_data(self, table_name: str, where: str):
        pass
