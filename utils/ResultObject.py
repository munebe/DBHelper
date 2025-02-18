from pandas import DataFrame


class ResultObject:
    def __init__(self, isSuccess: bool = False, message: str = None, data: DataFrame = None):
        self.isSuccess = isSuccess
        self.message = message
        self.data = data
