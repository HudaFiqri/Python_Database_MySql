###import module
import Connection

###eksekusi perintah
DB_Connect = Connection.DB_Connect.cursor()
DB_Connect.execute('SELECT * FROM User_Data')

for x in DB_Connect:
    print('\nId = ', x[0])
    print('nama user = ', x[1])
    print('password user = ', x[2])