###import module
import mysql.connector

###membuat koneksi ke server
username = 'cperoot'
password = 'nasional123'
server = 'localhost'
database = 'Local'

###authentikasi ke server
DB_Connect = mysql.connector.connect(user=username, password=password, host=server, database=database)

###eksekusi perintah
DB_Cursor = DB_Connect.cursor()
#untuk user
DB_Cursor.execute('DELETE FROM User_Data WHERE nama = "user1"')
#untuk ID
DB_Cursor.execute('DElETE FORM User_Data WHERE ID = 1')

###jangan lupa datanya commit ke server
DB_Connect.commit()
###tampilkan data dari server
DB_Cursor.execute('SELECT * From User_Data')

for x in DB_Cursor:
    print('id =', x[0])
    print('nama user = ', x[1])
    print('nama password =', x[2])
