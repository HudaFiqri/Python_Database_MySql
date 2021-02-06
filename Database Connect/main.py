###import module koneksi
import koneksi

###eksekusi perintah
cursor = koneksi.koneksi.cursor()
cursor.execute('show databases')

###tampilkan database
for x in cursor:
    print(x)
