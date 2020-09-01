from kafka import KafkaConsumer

# Consumer configured to consume latest messages and auto-commit offsets
consumer = KafkaConsumer('my-topic', # topic to listen
                         group_id='my-group', # join the my-group group
                         bootstrap_servers='localhost:9092')

print("Consumer started")
try:
    while True:
        for message in consumer:
            # topic:partition:offset key=key value=msg
            print("%s:%d:%d key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
except KeyboardInterrupt: # stop the consumer when any key is pressed
    consumer.close()
    pass
print("Consumer stopped")