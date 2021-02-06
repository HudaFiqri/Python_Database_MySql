###import module yang diperlukan
from mysql import connector

###koneksi server
server = ("localhost")
username = ("cperoot")
password = ("nasional123")
database = ("Local")

###membuat koneksi ke server dan authentikasi
DB_Connect = connector.connect(host=server, user=username, password=password, database=database)