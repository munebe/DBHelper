
from Connectors.MsSqlConnector import MsSqlConnector
import pandas as pd
import datetime


conn = MsSqlConnector(server='192.168.1.185', user='sa',
                      password='qwer1234.', database='test', port=1433)


df = pd.DataFrame({'string_field': ['string1', 'string2', 'string3'],
                   'int_field': [1, 2, 3],
                   'float_field': [1.1, 2.2, 3.3],
                   'date_field': [datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 2), datetime.datetime(2021, 1, 3)],
                   'datetime_field': [datetime.datetime(2021, 1, 1, 1, 1, 1), datetime.datetime(2021, 1, 2, 2, 2, 2), datetime.datetime(2021, 1, 3, 3, 3, 3)],
                   'bool_field': [True, False, True]
                   })


res = conn.query_to_df('SELECT * FROM test_table')
print(res.data)
