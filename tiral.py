import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='nahom#db', database="my_new_db")

mycursor = mydb.cursor()

mycursor.execute("select * from users")

result = mycursor.fetchone()

for i in result:
    print(i)

