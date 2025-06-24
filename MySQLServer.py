import mysql.connector

alxdb = mysql.connector.connect(host='localhost', user='root', passwd='randompassword')

dbcursor = alxdb.cursor()   

try:
    dbcursor.execute(" CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error:
    print('Database connection failed!')
