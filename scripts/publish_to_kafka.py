from kafka import KafkaProducer
import json

def publish_to_kafka():
    """
    Publishes the generated JSON data to a Kafka topic.
    
    Returns:
        None
    Raises:
        FileNotFoundError: If the JSON file is not found.
        Exception: If Kafka connection fails.
    """
    # Initialize Kafka producer
    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    except Exception as e:
        print(f"Failed to connect to Kafka: {e}")
        raise
    
    # Load the generated data
    try:
        with open("/tmp/generated_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError as e:
        print(f"Generated data file not found: {e}")
        raise
    
    # Publish each record to the Kafka topic
    for record in data:
        producer.send('data_topic', record)
    producer.flush()
    producer.close()
    print("Data published to Kafka topic 'data_topic'.")

if __name__ == "__main__":
    publish_to_kafka()