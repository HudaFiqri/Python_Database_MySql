###import module yang diperlukan
from mysql import connector

###membuat config authentikasi
server = "localhost"
username = "cperoot"
password = "nasional123"
database = "Local"

###membuat authentikasi ke server
DB_Connect = connector.connect(host=server, user=username, password=password, database=database)