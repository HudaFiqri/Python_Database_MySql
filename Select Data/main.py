###import directory
import Connection

###eksekusi perintah ke server
DB_Connect = Connection.DB_Cursor.cursor()
DB_Connect.execute("SELECT * FROM User_Data")

###mengambil data dalam database dan menghitungnya
DB_Data = DB_Connect.fetchall()

###menampilkan banyaknya data dalam table
print("Banyaknya Data Dalam Database adalah", DB_Connect.rowcount)

for data in DB_Data:
    print("id =", data[0])
    print("nama =", data[1])
    print("password =", data[2])
    print("\n")

