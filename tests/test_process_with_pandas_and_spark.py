import unittest
import os
from unittest.mock import patch, MagicMock
from scripts.process_with_pandas_and_spark import process_with_pandas, process_with_spark

class TestProcessWithPandasAndSpark(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy CSV file for testing.
        """
        os.makedirs("/tmp", exist_ok=True)
        with open("/tmp/remote_data.csv", "w") as f:
            f.write("column_name\n100\n200\n")

    def test_process_with_pandas(self):
        """
        Test the Pandas processing function.
        """
        process_with_pandas()
        self.assertTrue(os.path.exists("/tmp/pandas_processed.csv"))

    @patch('scripts.process_with_pandas_and_spark.SparkSession')  # Patch the SparkSession in the correct module
    def test_process_with_spark(self, mock_spark_session):
        """
        Test the Spark processing function.
        """
        # Create a mock Spark session
        mock_spark = MagicMock()
        mock_spark_session.builder.appName.return_value.getOrCreate.return_value = mock_spark
        
        # Mock the read.csv method
        mock_df = MagicMock()
        mock_spark.read.csv.return_value = mock_df
        
        # Mock the DataFrame's __getitem__ method (df["column_name"])
        mock_column = MagicMock()
        mock_df.__getitem__.return_value = mock_column
        
        # Mock the comparison operation (df["column_name"] > 100)
        mock_condition = MagicMock()
        mock_column.__gt__.return_value = mock_condition
        
        # Mock the filter method
        mock_filtered_df = MagicMock()
        mock_df.filter.return_value = mock_filtered_df
        
        # Run the Pandas processing first
        process_with_pandas()
        
        # Run the Spark processing
        process_with_spark()
        
        # Verify Spark session initialization
        mock_spark_session.builder.appName.assert_called_once_with("SparkProcessing")
        
        # Verify CSV read
        mock_spark.read.csv.assert_called_once_with("/tmp/pandas_processed.csv", header=True, inferSchema=True)
        
        # Verify column access and comparison
        mock_df.__getitem__.assert_called_once_with("column_name")
        mock_column.__gt__.assert_called_once_with(100)
        
        # Verify filter was called with the mock condition
        mock_df.filter.assert_called_once_with(mock_condition)
        
        # Verify write to CSV
        mock_filtered_df.write.mode.assert_called_once_with("overwrite")
        mock_filtered_df.write.mode().csv.assert_called_once_with("/tmp/spark_processed.csv")
        
        # Verify cleanup
        mock_spark.stop.assert_called_once()

if __name__ == "__main__":
    unittest.main()