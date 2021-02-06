from mysql import connector

host = ('localhost')
user = ('cperoot')
password = ('nasional123')
database = ('Local')

koneksi = connector.connect(host=host, user=user, password=password, database=database)

cursor_connect = koneksi.cursor()