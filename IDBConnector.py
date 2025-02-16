from abc import ABC, abstractmethod
from pandas import DataFrame


class IDBConnector(ABC):
    @abstractmethod
    def query_to_df(self, query: str):
        pass
    @abstractmethod
    def column_name_to_df(self, table_name: str):
        pass

    @abstractmethod
    def insert_df(self, df: DataFrame, table_name: str):
        pass

    @abstractmethod
    def truncate_table(self, table_name: str):
        pass

    @abstractmethod
    def delete_data(self, table_name: str, where: str):
        pass
