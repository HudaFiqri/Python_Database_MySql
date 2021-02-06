import mysql.connector

username = 'cperoot'
password = 'nasional123'
server = 'localhost'
database = 'Local'

try:
    DB_Connect = mysql.connector.connect(user=username, password=password, host=server, database=database)

except:
    print('Connection Eror')