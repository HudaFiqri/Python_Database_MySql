###import module yang diperlukan
import mysql.connector

###membuat koneksi ke server
username = 'cperoot'
password = 'nasional123'
server = 'localhost'
database = 'Local'

###authentikasi ke server
DB_Connect = mysql.connector.connect(user=username, password=password, host=server, database=database)