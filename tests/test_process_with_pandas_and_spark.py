import unittest
from scripts.process_with_pandas_and_spark import process_with_pandas, process_with_spark
import os

class TestProcessWithPandasAndSpark(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy CSV file for testing.
        """
        with open("/tmp/remote_data.csv", "w") as f:
            f.write("column_name\n100\n200\n")

    def test_process_with_pandas(self):
        """
        Test the Pandas processing function.
        """
        process_with_pandas()
        self.assertTrue(os.path.exists("/tmp/pandas_processed.csv"))

    def test_process_with_spark(self):
        """
        Test the Spark processing function.
        """
        process_with_pandas()
        process_with_spark()
        self.assertTrue(os.path.exists("/tmp/spark_processed.csv"))

if __name__ == "__main__":
    unittest.main()