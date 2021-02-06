from mysql import connector

hostname = ('localhost')
username = ('cperoot')
password = ('nasional123')
database = ('Local')

koneksi = connector.connect(host=hostname, user=username, password=password, database=database)

DB_Cur = koneksi.cursor()
DB_Cur.execute('show databases')

for x in DB_Cur:
    print(x)