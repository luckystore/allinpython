import mysql.connector

con = mysql.connector.connect(user='root', password='password', host='localhost',database='mysql')
cur = con.cursor()
cur.execute("""
              select * from mysql.credit_feeds where NOTIFICATION_STATUS = 'UNSENT'
              """)
row = cur.fetchall()
print(row)
cur.close()