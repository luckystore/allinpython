from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
#for _ in range(100):
producer.send('FeedTopic', b'2,WellsForgo,Savings,2,3589787654,David Miller,$850,1532490000000,1532320000000,ECS')
    # This is important
producer.flush()