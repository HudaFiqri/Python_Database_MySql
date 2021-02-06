###import module yang diperlukan
import mysql.connector

###buat authentikasi ke server
host = ('localhost')
user = ('cperoot')
password = ('nasional123')
database = ('Local')

###buat koneksi ke server
koneksi = mysql.connector.connect(host=host, user=user, password=password, database=database)
