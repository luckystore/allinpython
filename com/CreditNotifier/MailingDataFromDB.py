import smtplib
import  MySQLdb

SERVER = "localhost"

gmail_user = "kiranmekanuri@gmail.com"
gmail_password = "XXXXX"

FROM = gmail_user
TO = ["kiranmekanuri@gmail.com"]
Subject ="Hello"
Body=""

db = MySQLdb.connect(host='localhost', user='root', password='password', db='mysql')
cursor = db.cursor()
cursor.execute("""
              select * from mysql.kafkatable

              """)
rows = cursor.fetchall()
for item in rows:
    #Body+''.join(item)
    #print(Body+''.join(item))
    Body = Body+''.join(item)


print(Body)
TEXT = "This message was sent with python's."
message = """Subject: %s\n\n%s
    """ % (Subject, Body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(FROM,TO,message)
    server.close()
except:
    print('Something went wrong...')
