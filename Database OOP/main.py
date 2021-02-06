###import Directorynya
import Connection

###import dan execute filenya
DB_Cursor = Connection.DB_Connect.cursor()
DB_Cursor.execute("drop database Local3")
DB_Cursor.execute("show databases")

for x in DB_Cursor:
    print(x)