from kafka import KafkaProducer
import os
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

print("Producer started")
try:
    i = 0
    while True:
        producer.send('my-topic', bytearray('msg_' + str(os.getpid()) + ":" + str(i), 'UTF-8'))
        i = i + 1
        time.sleep(2)
except KeyboardInterrupt:
    producer.close()
    pass
print("producer stopped")