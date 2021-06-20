import pandas as pd
import mysql.connector
from datetime import datetime
from random import random, seed

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pen@2021",
    database="tentpole"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# View All Database
for x in mycursor:
  print(x)

def parseExcel(filePath):
      mycursor = mydb.cursor()
      col_names = ['created','incomes','expenses']
      excelData = pd.read_excel(filePath,names=col_names, header=None)
      for i,row in excelData.iterrows():
             sql = "INSERT INTO tentpole.test1 (created, incomes, expenses) VALUES (%s, %s, %s)"
             val = (row['created'],row['incomes'],row['expenses'])
             mycursor.execute(sql, val)
             mydb.commit()
             print(i,row['created'],row['incomes'],row['expenses'])


         