from abc import ABC, abstractmethod
from pandas import DataFrame
import ResultObject


class IDBConnector(ABC):

    def __init__(self, server: str, port: int, user: str, password: str, database: str = None):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    @abstractmethod
    def test_connection(self) -> ResultObject:
        pass

    @abstractmethod
    def query_to_df(self, query: str) -> ResultObject:
        pass

    @abstractmethod
    def column_name_to_df(self, table_name: str) -> ResultObject:
        pass

    @abstractmethod
    def insert_df(self, df: DataFrame, table_name: str) -> ResultObject:
        pass

    @abstractmethod
    def truncate_table(self, table_name: str) -> ResultObject:
        pass

    @abstractmethod
    def delete_data(self, table_name: str, where: str) -> ResultObject:
        pass
