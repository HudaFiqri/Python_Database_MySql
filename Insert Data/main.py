###import module
import Connection

###Query yang akan dimasukkan ke server
DB_Query = "INSERT INTO User_Data (Nama) VALUES ('Linfiq2')"

###execute program
DB_Cursor = Connection.DB_Connect.cursor()
DB_Cursor.execute(DB_Query)

###setelah di execute di atas commit datanya ke server
Connection.DB_Connect.commit()