import unittest
from unittest.mock import patch, MagicMock
from scripts.spark_streaming_2 import spark_streaming_2

class TestSparkStreaming2(unittest.TestCase):
    @patch('pyspark.sql.SparkSession.builder')  # Mock the SparkSession
    def test_spark_streaming_2(self, mock_spark_builder):
        """
        Test the spark_streaming_2 function to ensure it sets up a Kafka stream correctly.
        """
        # Create a mock Spark session
        mock_spark = MagicMock()
        mock_spark_builder.appName.return_value.getOrCreate.return_value = mock_spark
        
        # Mock the readStream and writeStream methods
        mock_df = MagicMock()
        mock_spark.readStream.format.return_value.option.return_value.option.return_value.load.return_value = mock_df
        mock_df.selectExpr.return_value = mock_df
        
        mock_query = MagicMock()
        mock_df.writeStream.outputMode.return_value.format.return_value.option.return_value.option.return_value.start.return_value = mock_query
        
        # Run the function
        spark_streaming_2()
        
        # Verify that Spark session was initialized
        mock_spark_builder.appName.assert_called_once_with("SparkStreaming2")
        
        # Verify Kafka streaming setup
        mock_spark.readStream.format.assert_called_once_with("kafka")
        mock_spark.readStream.format().option.assert_any_call("kafka.bootstrap.servers", "kafka:9092")
        mock_spark.readStream.format().option().option.assert_any_call("subscribe", "data_topic")
        
        # Verify output setup
        mock_df.writeStream.outputMode.assert_called_once_with("append")
        mock_df.writeStream.outputMode().format.assert_called_once_with("json")
        mock_df.writeStream.outputMode().format().option.assert_any_call("path", "/tmp/kafka_output")
        mock_df.writeStream.outputMode().format().option().option.assert_any_call("checkpointLocation", "/tmp/checkpoints")
        
        # Verify termination and cleanup
        mock_query.awaitTermination.assert_called_once_with(60)
        mock_spark.stop.assert_called_once()

if __name__ == "__main__":
    unittest.main()