from elasticsearch import Elasticsearch
import json
import os

def index_to_elasticsearch():
    """
    Indexes the Kafka output JSON files into Elasticsearch.
    
    Returns:
        None
    Raises:
        Exception: If Elasticsearch connection or indexing fails.
    """
    # Initialize Elasticsearch client
    try:
        es = Elasticsearch(['http://elasticsearch:9200'])
    except Exception as e:
        print(f"Failed to connect to Elasticsearch: {e}")
        raise
    
    # Index each JSON file from the Kafka output
    for file_name in os.listdir("/tmp/kafka_output"):
        file_path = os.path.join("/tmp/kafka_output", file_name)
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                es.index(index="data_index", body=data)
        except Exception as e:
            print(f"Failed to index {file_name} into Elasticsearch: {e}")
            raise
    print("Data indexed in Elasticsearch index 'data_index'.")

if __name__ == "__main__":
    index_to_elasticsearch()