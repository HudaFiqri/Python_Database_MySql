from mysql import connector

#Create Database Connection
DB_Connect = connector.connect(user="cperoot", password="nasional123", host='localhost')

#Create Database Cursor
DB_Cursor = DB_Connect.cursor()
DB_Cursor.execute('CREATE DATABASE Local2')
DB_Cursor.execute('show databases')

#Show Database
for data in DB_Cursor:
    print(data)