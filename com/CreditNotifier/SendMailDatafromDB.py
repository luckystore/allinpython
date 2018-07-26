import mysql.connector
import smtplib

gmail_user = "kiranmekanuri@gmail.com"
gmail_password = "XXXXXX"

From = gmail_user
To = ["kiranmekanuri@gmail.com"]
Subject = "Hello From Python Email Sender"
Body = "a"
message = """Subject: %s\n\n%s
    """ % (Subject, Body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(From,To,message)
    server.close()
except:
    print('Something went wrong...')


con = mysql.connector.connect(user='root', password='password', host='localhost',database='mysql')
cur = con.cursor()
cur.execute("""
              select * from mysql.kafkatable

              """)
row = cur.fetchall()
print(row[1])
cur.close()
a = ('row')
string = ' '.join(a)




#a = ('write', 'a', 'program')
#string = ' '.join(a)
#print(string)