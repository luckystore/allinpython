import smtplib
import  MySQLdb
import datetime

date = ''
SERVER = "localhost"

gmail_user = "kiranmekanuri@gmail.com"
gmail_password = "venkeykiran"

FROM = gmail_user
TO = ["kiranmekanuri@gmail.com"]
#Subject = "Hello"
Body = ""


db = MySQLdb.connect(host='localhost', user='root', password='password', db='mysql')
cursor = db.cursor()
cursor.execute("""

              select cf.FI,cf.ACCOUNT_NO,cd.CUSTOMER_NAME,cf.AMOUNT_DUE_IN_DOLLERS,cf.DUE_DATE,cd.CUSTOMER_EMAIL from credit_feeds cf,
               customer_details cd where cf.CUSTOMER_ID = cd.ID 
              """)
rows = cursor.fetchall()
for item in rows:
     fi = item[0]
     account_no = item[1]
     customer_name = item[2]
     due_amount = item[3]
     due_date = item[4]
     email = item[5]
     due_date = due_date[:-3]

     account_no = ''.join(item[1])
     customer_name = ''.join(item[2])
     due_amount =''.join(item[3])
     due_date = datetime.datetime.fromtimestamp(int(due_date)).strftime('%Y-%m-%d %H:%M:%S')
     print(due_date)
print(item)

TEXT = "Regarding Loan Amount - {}".format(fi)+"\n"\
    "Dear {},".format(customer_name)+ "\n" \
       "                  This mail from your bank, regarding your loan. " \
       "Your loan mount is  {}".format(due_amount)+ " " +\
       "and the due date  {}.".format(due_date)+ " " + "Please keep Funds in your account. " \
       "Your account number is  {}.".format(account_no)+ "\n" \
       "                                                                                                                " \
       "                                                                                                               " \
       "            Thank you...                                                                                       " \
       "                                                                                                              " \
       "                                                {},".format(fi)



message = """Subject: %s %s
    """ % (Body, TEXT)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user,gmail_password)
    server.sendmail(FROM,TO,message)
    server.close()
except:
     print('Something went wrong...')
