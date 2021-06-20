import mysql.connector
from datetime import datetime
from random import random, seed


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pen@2021",
    database="tentpole"
)

def insert_user(first_name, last_name,dob):
    mycursor = mydb.cursor()

    seed(datetime.now())

    sql = "INSERT INTO tentpole.user (userid, firstname, lastname, dob) VALUES (%s,%s,%s,%s)"
    val = (int(random()*1000),first_name, last_name, dob)
    mycursor.execute(sql, val)

    mydb.commit()

    return