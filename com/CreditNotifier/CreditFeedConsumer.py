from kafka import KafkaConsumer

consumer = KafkaConsumer('FeedTopic')
for msg in consumer:
    kafka_msg = msg.value.decode('utf-8')
    print(kafka_msg)