from kafka import KafkaConsumer
import redis
import time
import pymysql
from datetime import datetime

consumer = KafkaConsumer('metrics')
redisserver = redis.Redis()


conn = pymysql.connect(host='localhost', user='root', password='root', db='world')
a = conn.cursor()
add_temperature_sql = ("""
                            insert into world.device_temperature
                            (time_sec,Temperature) 
                            values(%s,%s)
                            
                            """)
now_timestamp = datetime.now()

for msg in consumer:
    conValue = int.from_bytes(msg.value,'big')
    print(conValue)
    millis = int(round(time.time() * 1000))
    redisserver.set(millis,conValue)
    data = (now_timestamp,conValue)
    try:
        a.execute(add_temperature_sql,data)
        conn.commit()
    except:
        conn.rollback()

conn.close()
