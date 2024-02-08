import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '125863' 
)

# prepare a cursor object
cursorObject = database.cursor()

#create a database. 
cursorObject.execute("CREATE DATABASE website")
print("All Done")