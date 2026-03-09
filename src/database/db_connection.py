import mysql.connector

def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mysql@2380",
        database="expense_tracker"   # your DB name
    )
    return connection