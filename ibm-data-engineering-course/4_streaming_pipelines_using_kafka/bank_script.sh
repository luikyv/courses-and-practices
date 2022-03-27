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
exec bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic bankbranch --partitions 2
# List all the topics to see if bankbranch has been created successfully
exec bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
# use the --describe command to check the details of the topic bankbranch
exec bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch

# bankbranch has two partitions Partition 0 and Partition 1.
# If no message keys are specified, messages will be published to
# these two partitions in an alternating sequence, like this:
# Partition 0 -> Partition 1 -> Partition 0 -> Partition 1 -> ...

# You need a producer to send messages to Kafka. Run the command below to start a producer
exec bin/kafka-console-producer.sh --topic bankbranch --bootstrap-server localhost:9092
# Consumer
exec bin/kafka-console-consumer.sh --topic bankbranch --bootstrap-server localhost:9092

# Messages with the same key will always be published to the same partition,
# so that their published order will be preserved within the message queue of each partition
# Start a new producer with message key enabled
exec bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch --property parse.key=true --property key.separator=:
# Consumer
exec bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --from-beginning --property print.key=true --property key.separator=:

# Create a consumer group
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

# Show the details of the consumer group atm-app
exec bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --group atm-app

# reset the index with the --reset-offsets argument
exec bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --to-earliest --execute

# Reset the offset so that we only consume the last two messages.
exec bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092  --topic bankbranch --group atm-app --reset-offsets --shift-by -2 --execute