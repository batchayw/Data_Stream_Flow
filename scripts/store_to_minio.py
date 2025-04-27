from minio import Minio
import os

def store_to_minio():
    """
    Stores the Kafka output JSON files in MinIO.
    
    Returns:
        None
    Raises:
        Exception: If MinIO connection or upload fails.
    """
    # Initialize MinIO client
    try:
        client = Minio(
            "minio:9000",
            access_key="minioadmin",
            secret_key="minioadmin",
            secure=False
        )
    except Exception as e:
        print(f"Failed to connect to MinIO: {e}")
        raise
    
    # Ensure the bucket exists
    bucket_name = "data-bucket"
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    
    # Upload each JSON file from the Kafka output
    for file_name in os.listdir("/tmp/kafka_output"):
        file_path = os.path.join("/tmp/kafka_output", file_name)
        try:
            client.fput_object(bucket_name, f"data/{file_name}", file_path)
        except Exception as e:
            print(f"Failed to upload {file_name} to MinIO: {e}")
            raise
    print("Data stored in MinIO bucket 'data-bucket'.")

if __name__ == "__main__":
    store_to_minio()