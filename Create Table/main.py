###import directorynya
import Connection

###execute perintah
Connect = Connection.DB_Connect.cursor()
Connect.execute("CREATE TABLE User_Data3 (ID INT(4), Nama CHAR(100))")
DB = Connect.execute("SELECT * FROM User_Data3")

print(DB)