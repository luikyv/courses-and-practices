# Introduction to Apache Kafka

If you have 4 source systems, and 6 target systems, you need 24 integrations to share information among them all where each integration have its specifications such as protocol, data format and so on. Also, each source system will have an increased load from the connections.

Created by LinkedIn, Apache Kafka is an open-source project that comes to solve this problem by decoupling the data streams and the systems. Moreover, Apache Kafka is distributed, has a resilient architecture and is fault tolerante.

Some of the applications of Apache Kafka are:
* Messaging System
* Activity Tracking
* Gather metrics from many different locations

## Kafka Topics
A topic is a stream of data. It's like a table for databases, but without the constraints, since it can handle any kind of data.

Kafka is a data stream platform since you can stream data through topics.

Topics are split in partitions where messages are orderly stored.

Each message within a partition gets an incremental id, called offset.

Topics are **immutable** meaning that once data is written to a partition, it cannot be changed.

Data is kept only for an limited amount of time (default to one week). However the offsets will alwats keep increasing.

## Producers
Producers write data to topics and they know in advance to which partition they will write the content (by the hash applied to the key).

Producers can send messages with keys. If no key is sent, the messages will be attributed to the partitions in round robin. Otherwise, **messages with the same key are stored in the same partition** by using a hash (default is the murmur2 algorithm).

The key and values sent by producers are serialized in the messages (messages are more than key and value).

## Consumers
Consumers read data (in order from low to high offset) from a topic - pull model. They know which broker to read from.

In order to deserialize the keys and values from messages, the consumer needs to know their formats.

The serialization/deserialization type must not change during a topic lifecycle. **If you need to change the serialization format, you must create a new topic instead**.

## Consumer Groups
A group defines an application.

Each consumer within a group reads from exclusive partitions.

If you have more consumers than partitions, some consumers will be inactive.

## Consumer Offsets
Kafka stores the offsets at which consumer has been reading. These offsets are committed in the topic and named __consumer_offsers.

Consumers periodically commit the offsets. By doing so, they are telling how far they have been successfully reading into the Kafka topic.

## Kafka Brokers
A broker is a server (bootstrap server) in Kafka. It receives and sends data by storing topic partitions.

Each broker contains certain topic partitions, that means the data is distributed among the brokers.

After connecting to a broker, the Kafka clients will know how to connect to the entire cluster, since each broker knows all about brokers, topics and partitions.

## Topic replication factor
If a broker is down, another broker can serve the data.

At any time **only one broker can be a leader for a given partition** and the other brokers will replicate the data.

Producers can only write to the leader broker for a partition. Consumers by default only read from the leader broker for a partition.

## Kafka Consumers Replica Fetching
Consumers can read from the closest replica to improve latency and decrease network costs.

## Zookeeper
It manages brokers. It sends notifications to Kafka in case of changes.

It's being deprecated

## Static Group Membership
By default, when a cosumer leaves a group, its partitions are revoked and re-assigned. If it joins back, it will have a new member id and new partitions assigned.

If you specify a group.instance.id it makes the consumer **static member**. Then, upon leaving, the consumer has up to session.timeout.ms to join back and get back its partitions, without triggering a rebalance.

## Producer Acknowledgments
Producers can choose to receive acknowledgments of data writes.
* Acks = 0: Producer won't wait for acknowledgment (Possible data loss)
* Acks = 1: Producer will wait for leader acknowledgment (Limeted data loss)
* Acks = all(-1): Leader + replicas acknowledgment (No data loss)

Common configuration: partitions=3, min.insync.replicas=2 and acks=all.

When acks=all, replication.factor=N and min.insync.replicas=M, we can tolerate at most N-M brokers going down for topic availability purposes.
