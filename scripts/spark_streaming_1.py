from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

def spark_streaming_1():
    """
    Streams the Spark-processed CSV file using Spark Streaming and outputs to the console.
    
    Returns:
        None
    Raises:
        Exception: If streaming fails.
    """
    # Initialize a Spark session for streaming
    spark = SparkSession.builder.appName("SparkStreaming1").getOrCreate()
    
    # Define the schema of the CSV file
    # Replace with the actual schema of your CSV
    schema = StructType([StructField("column_name", StringType(), True)])
    
    # Read the CSV file as a streaming DataFrame
    try:
        streaming_df = spark.readStream.schema(schema).csv("/tmp/spark_processed.csv")
    except Exception as e:
        print(f"Failed to read CSV as stream: {e}")
        spark.stop()
        raise
    
    # Write the stream to the console (for testing)
    query = streaming_df.writeStream.outputMode("append").format("console").start()
    
    # Run the streaming for 60 seconds (adjust as needed)
    query.awaitTermination(60)
    spark.stop()
    print("Spark Streaming 1 completed.")

if __name__ == "__main__":
    spark_streaming_1()