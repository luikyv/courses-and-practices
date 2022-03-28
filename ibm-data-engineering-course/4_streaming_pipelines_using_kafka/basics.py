import json
from kafka.admin import KafkaAdminClient, NewTopic, ConfigResource, ConfigResourceType
from kafka.producer import KafkaProducer
from kafka.consumer import KafkaConsumer

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id="test"
)
new_topic = NewTopic(
    name="bankbranch",
    num_partitions=2,
    replication_factor=1,
)

admin_client.create_topics(new_topics=[new_topic])

configs = admin_client.describe_configs(config_resources=[
    ConfigResource(ConfigResourceType.TOPIC, "bankbranch")
])

producer = KafkaProducer(
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})

consumer = KafkaConsumer("bankbranch")
for msg in consumer:
    print(msg.value.decode("utf-8"))