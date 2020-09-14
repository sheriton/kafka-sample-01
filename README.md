## Requirements

 - Docker
 - Images: 
    - wurstmeister/kafka
    - wurstmeister/zookeeper
 - Python
 - kafka-python 

## Usage

First, run the command below to start zookeeper and kafka
```bash
docker-compose up -d
```

To start a producer
```
python3 example/producer.py
````

Each producer will write a message in the format: 
```
_msg_<process_id>:<msg_id>_
```
 - _<process_id>_: OS process id (pid) of the producer
 - _<msg_id>_: sequential integer starting in 0

To start a consumer
```
python3 example/consumer.py
```
The consumer reads a message and prints it in the format: 
```
_topic:partition:offset key=key value=msg_
```

Producers will write to the topic 'my-topic' and consumers will read from 'my-topic'. All consumers are part of 'my-group', it means that only one consumer will of the group will receive a message written to a partition of 'my-topic'.
The topic will be created automatically when you start a producer. But, if you want to start the topic before start the application, you can do it running the following command in the kafka cli.
```bash
kafka-topics.sh --zookeeper zookeepeer:2181 --create --topic my-topic --partitions <number_of_partitions> --replication-factor <number_of_replicas_for_each_partition>
```

To change the number of partitions of the topic, run the command in the kafka cli. You can change the number of partitions on the go.
```bash
kafka-topics.sh --zookeeper zookeeper:2181 --alter --topic my-topic --partitions 2
```

_Remeber that each **partition** will be read **exclusively** by one **consumer**. So if you want all your consumers to read at least one partition, make sure you have at least as many partitions as consumers._ 


Kafka decides in which partition each message will be written, so you cannot guarantee what message a consumer will receive.