###import module yang diperlukan
import mysql.connector

###membuat config authentikasi
username = 'cperoot'
password = 'nasional123'
server = 'localhost'
database = 'Local'

###testing koneksi dengan server apakah berhasil atau tida
try:
    DB_Connect = mysql.connector.connect(user=username, password=password, host=server, database=database)

except:
    print('Connection Eror')
