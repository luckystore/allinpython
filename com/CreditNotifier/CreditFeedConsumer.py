from kafka import KafkaConsumer
# import time
import pymysql
from datetime import datetime

consumer = KafkaConsumer('FeedTopic')
# redisserver = redis.Redis()


conn = pymysql.connect(host='localhost', user='root', password='password', db='mysql')
a = conn.cursor()
add_temperature_sql = ("""
                            insert into mysql.credit_feeds
                            (FI, ACCOUNT_TYPE, CUSTOMER_ID, ACCOUNT_NO,ACCOUNT_HOLDER,AMOUNT_DUE_IN_DOLLERS,
                            DUE_DATE,DUE_REMAINDER_DATE,DUE_CLEARANCE_MODE) 
                            values(%s, %s, %s, %s, %s, %s, %s, %s, %s)

                            """)

for msg in consumer:
    try:
        messageByte = msg.value.decode("utf-8")
        fi = messageByte.split(',')[1]
        account_type = messageByte.split(',')[2]
        customer_id = messageByte.split(',')[3]
        account_no = messageByte.split(',')[4]
        account_holder_name = messageByte.split(',')[5]
        amount_due_in_dollers = messageByte.split(',')[6]
        due_date = messageByte.split(',')[7]
        due_date_remainder = messageByte.split(',')[8]
        due_clearance_mode = messageByte.split(',')[9]

        a.execute(add_temperature_sql, (fi, account_type, customer_id, account_no,account_holder_name,
                                        amount_due_in_dollers,due_date,due_date_remainder,due_clearance_mode))
        conn.commit()
        print("Data has been saved into CREDIT_FEEDS Table")
    except Exception as e:
        print(e)
        conn.rollback()

conn.close()
