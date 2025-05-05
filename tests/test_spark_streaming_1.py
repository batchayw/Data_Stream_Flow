import unittest
from unittest.mock import patch, MagicMock
from scripts.spark_streaming_1 import spark_streaming_1

class TestSparkStreaming1(unittest.TestCase):
    @patch('scripts.spark_streaming_1.SparkSession')  # Patch the SparkSession in the correct module
    def test_spark_streaming_1(self, mock_spark_session):
        """
        Test the spark_streaming_1 function to ensure it sets up a CSV stream correctly.
        """
        # Create a mock Spark session
        mock_spark = MagicMock()
        mock_spark_session.builder.appName.return_value.getOrCreate.return_value = mock_spark
        
        # Mock the readStream and writeStream methods
        mock_df = MagicMock()
        mock_spark.readStream.schema.return_value.csv.return_value = mock_df
        mock_query = MagicMock()
        mock_df.writeStream.outputMode.return_value.format.return_value.start.return_value = mock_query
        
        # Run the function
        spark_streaming_1()
        
        # Verify that Spark session was initialized
        mock_spark_session.builder.appName.assert_called_once_with("SparkStreaming1")
        
        # Verify CSV streaming setup
        mock_spark.readStream.schema.assert_called_once()
        mock_spark.readStream.schema().csv.assert_called_once_with("/tmp/spark_processed.csv")
        
        # Verify output setup
        mock_df.writeStream.outputMode.assert_called_once_with("append")
        mock_df.writeStream.outputMode().format.assert_called_once_with("console")
        
        # Verify termination and cleanup
        mock_query.awaitTermination.assert_called_once_with(60)
        mock_spark.stop.assert_called_once()

if __name__ == "__main__":
    unittest.main()