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
                            (FI, ACCOUNT_TYPE, CUSTOMER_ID, ACCOUNT_NO) 
                            values(%s, %s, %s, %s)

                            """)

for msg in consumer:
    try:
        print(msg.value)
        messageByte = msg.value.decode("utf-8")
        print(type(messageByte))
        print(messageByte.split(',')[1])
        print(type(messageByte.split(',')[4]))
        print(messageByte.split(',')[4])
        fi = messageByte.split(',')[1]
        account_type = messageByte.split(',')[2]
        customer_id = messageByte.split(',')[3]
        account_no = messageByte.split(',')[4]

        a.execute(add_temperature_sql, (fi, account_type, customer_id, account_no))
        conn.commit()
    except:
        conn.rollback()

conn.close()
