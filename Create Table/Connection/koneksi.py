###import module yang diperlukan
from mysql import connector

###membuat koneksi dengan server
server = 'localhost'
username = 'cperoot'
password = 'nasional123'
database = 'Local'

###authentikasi dengan server
DB_Connect = connector.connect(host=server, user=username, password=password, database=database)
DB_Cursor = DB_Connect.cursor()