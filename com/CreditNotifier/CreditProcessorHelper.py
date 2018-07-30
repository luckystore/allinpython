import  MySQLdb
import datetime
import smtplib
from com.CreditNotifier.EmailDetails import EmailDetails

class CreditProcessorHelper:
    #mail details
    server = ""
    gmail_user = ""
    gmail_password = ""
    fromAddress = ""
    TO = []
    Body = ""

    #DB Details
    db_host = ""
    db_username=""
    db_password = ""
    db_schema = ""

    #customer Details
    fi = ""
    account_no = ""
    customer_name = ""
    due_amount = ""
    due_date = ""
    email = ""


    def CreditProcessorHelper(self, server,gmail_user,gmail_password,fromAddress,db_host,db_username,db_password,
                           db_schema):
        self.server = server
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password
        self.fromAddress = fromAddress

        self.db_host = db_host
        self.db_host = db_username
        self.db_password = db_password
        self.db_schema = db_schema




    def read_unsent_notifications(self):
        db = MySQLdb.connect(host='localhost', user='root', password='password', db='mysql')
        cursor = db.cursor()
        cursor.execute("""
                      select cf.FI,cf.ACCOUNT_NO,cd.CUSTOMER_NAME,cf.AMOUNT_DUE_IN_DOLLERS,cf.DUE_DATE,cd.CUSTOMER_EMAIL from credit_feeds cf,
                       customer_details cd where cf.CUSTOMER_ID = cd.ID 
                      """)
        EmailDetailsList = []
        rows = cursor.fetchall()
        for item in rows:
            self.fi = item[0]
            self.account_no = item[1]
            self.customer_name = item[2]
            self.due_amount = item[3]
            self.due_date = item[4]
            self.email = item[5]
            self.due_date = self.due_date[:-3]

            self.TO = [self.email]
            self.due_date = datetime.datetime.fromtimestamp(int(self.due_date)).strftime('%Y-%m-%d %H:%M:%S')
            print(self.due_date)
            print(item)
            person = EmailDetails(self.fi,self.account_no,self.customer_name,self.due_date,self.due_amount,self.email)
            EmailDetailsList.append(person)
        return EmailDetailsList


    def sendEmailNotification(self, EmailDetails):
     print("with in sendEmailNotification")
     print(self.TO)
     print(self.fi)
     self.TO = EmailDetails.email
     print("due date from emaildetails",EmailDetails.due_date)
     TEXT = "Regarding Loan Amount - {}".format(EmailDetails.fi)+"\n"\
             "Dear {},".format(EmailDetails.customer_name)+ "\n" \
                "                  This mail from your bank, regarding your loan. " \
                "Your loan mount is  {}".format(EmailDetails.due_amount)+ " " +\
                "and the due date  {}.".format(EmailDetails.due_date)+ " " + "Please keep Funds in your account. " \
                "Your account number is  {}.".format(EmailDetails.account_no)+ "\n" \
                "                                                                                                                " \
                "                                                                                                               " \
                "            Thank you...                                                                                       " \
                "                                                                                                              " \
                "                                                {},".format(EmailDetails.fi)
     message = """Subject: %s %s     """ % (self.Body, TEXT)
     try:
         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
         server.ehlo()
         server.login(self.gmail_user, self.gmail_password)
         server.sendmail(self.gmail_user, self.TO, message)
         server.close()
     except Exception as e:
         print(e)
         print('Something went wrong...')

    def updateNotificationStatus(self):
        pass

