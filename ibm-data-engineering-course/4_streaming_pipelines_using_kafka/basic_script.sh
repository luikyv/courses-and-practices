# Download kafka in the current directory
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

# Extract kafka from the zip file
tar -xzf kafka_2.12-2.8.0.tgz

cd kafka_2.12-2.8.0
# ZooKeeper, as of this version, is required for Kafka to work.
# ZooKeeper is responsible for the overall management of Kafka cluster.
# It monitors the Kafka brokers and notifies Kafka if any broker or partition goes down,
# or if a new broker or partition goes up.
# ZooKeeper is required for Kafka to work. Start the ZooKeeper server
exec bin/zookeeper-server-start.sh config/zookeeper.properties

# In a new terminal start the Kafka message broker service
exec bin/kafka-server-start.sh config/server.properties

# Start a new terminal
# Run the command below to start a new topic
exec bin/kafka-topics.sh --create --topic news --bootstrap-server localhost:9092

# You need a producer to send messages to Kafka. Run the command below to start a producer
exec bin/kafka-console-producer.sh --topic news --bootstrap-server localhost:9092

# In a new terminal, create a consumer to read messages from kafka
exec bin/kafka-console-consumer.sh --topic news --from-beginning --bootstrap-server localhost:9092