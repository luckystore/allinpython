from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(100):
    producer.send('FeedTopic', b'I am stored in db')
    # This is important
producer.flush()