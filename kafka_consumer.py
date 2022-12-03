from kafka import KafkaConsumer

consumer = KafkaConsumer('payments', bootstrap_servers='localhost:9092')

for msg in consumer:
    print("It is a new message!!!")
    print(msg)
