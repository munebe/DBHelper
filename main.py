from MySqlConnector import MySqlConnector
mySql = MySqlConnector(server='192.168.1.185', user='root',
                       password='qwer1234.', database='test', port=3306)
result = mySql.column_name_to_df('test_table')
print(result.data)
