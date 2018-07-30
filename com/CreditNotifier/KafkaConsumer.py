from kafka import KafkaConsumer
#import time
import pymysql
from datetime import datetime

consumer = KafkaConsumer('FeedTopic')
#redisserver = redis.Redis()


conn = pymysql.connect(host='localhost', user='root', password='password', db='mysql')
a = conn.cursor()
add_temperature_sql = ("""
                            insert into mysql.customer_details
                            
                            
                            values(%s)
                            
                            """)

for msg in consumer:
    try:
        print(msg.value)
        a.execute(add_temperature_sql, msg.value.decode('utf-8'))
        conn.commit()
    except:
        conn.rollback()

conn.close()
