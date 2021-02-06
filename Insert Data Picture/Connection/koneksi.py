###import module yang diperlukan
import mysql.connector

###buat config server
username = 'cperoot'
password = 'nasional123'
server = 'localhost'
database = 'Local'

try:
    ###membuat koneksi ke server dengan authentikasi
    DB_Connect = mysql.connector.connect(user=username, password=password, host=server, database=database)

except:
    print('koneksi gagal terhubung')