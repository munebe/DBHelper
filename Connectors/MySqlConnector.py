from Connectors.IDBConnector import IDBConnector
import mysql.connector
from utils.ResultObject import ResultObject
import pandas as pd


class MySqlConnector(IDBConnector):
    def __init__(self, server: str, port: int, user: str, password: str, database: str = None):
        super().__init__(server, port, user, password, database)

    def get_connection(self):
        return mysql.connector.connect(**{'host': self.server,
                                          'port': self.port,
                                          'user': self.user,
                                          'password': self.password,
                                          'database': self.database})

    def test_connection(self):
        try:
            with self.get_connection() as conn:
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
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(query)
                columns = [column[0] for column in cursor.description]
                result = cursor.fetchall()
                result_df = pd.DataFrame(result, columns=columns)

                return ResultObject(True, 'Query success', result_df)
        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))

    def table_name_to_df(self, table_name: str):
        try:
            with self.get_connection() as conn:
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
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()

                # Kolon isimlerini al
                columns = ', '.join(df.columns)
                # SQL'de güvenli parametre bağlama
                placeholders = ', '.join(['%s'] * len(df.columns))

                # SQL komutunu oluştur
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

                # DataFrame'i tuple listesine çevir
                values = [tuple(row) for row in df.to_numpy()]

                # Tüm satırları ekle
                cursor.executemany(query, values)

                # Değişiklikleri kaydet
                conn.commit()

                # Eklenen satır sayısını al
                inserted_row_count = cursor.rowcount

                return ResultObject(True, f'Data inserted successfully. Rows inserted: {inserted_row_count}')

        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))

    def truncate_table(self, table_name: str):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                query = f"TRUNCATE TABLE {table_name}"
                cursor.execute(query)

                return ResultObject(True, f'{table_name} truncated',)
        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))

    def execute_custom_dml(self, sql: str):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)

                conn.commit()
                affected_rows = cursor.rowcount

                return ResultObject(True, f'Success. Affected rows: {affected_rows}', affected_rows)
        except Exception as e:
            return ResultObject(False, 'Query failed: ' + str(e))
