###import module
import Connection

DB_Data = 'https://cupline.files.wordpress.com/2014/10/logo.gif'
DB_Image_Name = 'Debian 9 Image'

#INSERT INTO Other_Data (Name) VALUES ('http://1.bp.blogspot.com/-q2w0RBF6eSA/UylHlQHr-WI/AAAAAAAACnE/ZL7HpBFko6k/s280/smadav-terbaru.jpg')
DB_Query = f"INSERT INTO Other_Data (Name, Picture) VALUES ('{DB_Image_Name}', '{DB_Data}')"

###eksekusi perintah ke server
DB_Cursor = Connection.DB_Connect.cursor()
DB_Cursor.execute(DB_Query)

###commit filenya ke server
Connection.DB_Connect.commit()
