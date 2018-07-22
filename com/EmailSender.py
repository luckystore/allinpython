import smtplib

gmail_user = "kiranmekanuri@gmail.com"
gmail_password="XXXXXXXXXX"

From = gmail_user
To = ["kiranmekanuri@gmail.com"]
Subject = "Hello From Python Email Sender"
Body="Hi This is Kiran"
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