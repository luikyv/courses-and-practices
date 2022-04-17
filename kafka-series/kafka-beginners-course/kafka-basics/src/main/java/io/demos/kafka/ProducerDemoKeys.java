package io.demos.kafka;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.StringSerializer;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Properties;

public class ProducerDemoKeys {

    private static final Logger log = LoggerFactory.getLogger(ProducerDemoKeys.class.getSimpleName());

    public static void main(String[] args) {
        log.info("I am a Kafka Producer");

        // Create Producer properties
        Properties properties = new Properties();
        properties.setProperty(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "127.0.0.1:9092");
        properties.setProperty(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        properties.setProperty(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());

        // Create the Producer
        KafkaProducer<String, String> producer = new KafkaProducer<>(properties);

        for(int i=0; i<10; i++){

            String topic = "demo_java";
            String value = "hello world " + i;
            String key = "id_" + i;

            // Create a producer record
            ProducerRecord<String, String> producerRecord = new ProducerRecord<>(
                    topic,
                    key,
                    value
            );

            // Send the data - asynchronous
            producer.send(
                    producerRecord,
                    new Callback() {
                        @Override
                        public void onCompletion(RecordMetadata metadata, Exception exception) {
                            // Execute every time a record is successfully sent or an exception is thrown
                            if (exception == null) {
                                // The record was successfully sent
                                log.info(
                                        "Received new metadata \n" +
                                                "Topic: " + metadata.topic() + "\n" +
                                                "Key: " + producerRecord.key() + "\n" +
                                                "Partition: " + metadata.partition() + "\n" +
                                                "Offset: " + metadata.offset() + "\n" +
                                                "Timestamp: " + metadata.timestamp()
                                );
                            } else {
                                log.error("Error while producing", exception);
                            }
                        }
                    }
            );
        }

        // Flush and close the Producer - synchronous
        producer.flush();

        // Flush and close Producer
        producer.close();
    }
}
