import csv
import os
from kafka import KafkaProducer

file = open('C:\\Users\Sunil\\PycharmProjects\\allinpython\\com\\CreditNotifier\\CreditNotifyer22.csv')
readFile = csv.reader(file)

header = next(readFile)
first_row = next(readFile)
print(first_row)


producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('FeedTopic', bytes(first_row))
producer.flush()


dir(first_row)
#for item in first_row:
 #   p = p + ''.join(item)
print(header)
print(first_row)


