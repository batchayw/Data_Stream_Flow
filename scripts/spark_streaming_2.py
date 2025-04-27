from pyspark.sql import SparkSession

def spark_streaming_2():
    """
    Consumes data from a Kafka topic using Spark Streaming and saves it as JSON.
    
    Returns:
        None
    Raises:
        Exception: If streaming fails.
    """
    # Initialize a Spark session for streaming
    spark = SparkSession.builder.appName("SparkStreaming2").getOrCreate()
    
    # Read the Kafka stream
    try:
        df = spark.readStream.format("kafka") \
            .option("kafka.bootstrap.servers", "kafka:9092") \
            .option("subscribe", "data_topic") \
            .load()
    except Exception as e:
        print(f"Failed to read Kafka stream: {e}")
        spark.stop()
        raise
    
    # Convert the Kafka message value to a string
    df = df.selectExpr("CAST(value AS STRING)")
    
    # Write the stream to a JSON file
    query = df.writeStream.outputMode("append").format("json") \
        .option("path", "/tmp/kafka_output") \
        .option("checkpointLocation", "/tmp/checkpoints") \
        .start()
    
    # Run the streaming for 60 seconds (adjust as needed)
    query.awaitTermination(60)
    spark.stop()
    print("Spark Streaming 2 completed.")

if __name__ == "__main__":
    spark_streaming_2()