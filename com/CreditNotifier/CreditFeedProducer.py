from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
#for _ in range(100):
producer.send('FeedTopic', b'1, WellsForgo, Savings, 1, 3323232324, John, $750,1532490000000,1532320000000,ECS')
    # This is important
producer.flush()