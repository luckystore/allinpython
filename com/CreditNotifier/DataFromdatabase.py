import mysql.connector

con = mysql.connector.connect(user='root', password='password', host='localhost',database='mysql')
cur = con.cursor()
cur.execute("""
              select * from mysql.kafkatable

              """)
row = cur.fetchall()
print(row[1])
cur.close()