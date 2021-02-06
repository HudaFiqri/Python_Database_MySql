###import module yang diperlukan
import mysql.connector

###membuat config koneksi
username = 'cperoot'
password = 'nasional123'
server = 'localhost'
database = 'Local'

###membuat koneksi dan authentikasi ke server
DB_Cursor = mysql.connector.connect(user=username, password=password, host=server, database=database)