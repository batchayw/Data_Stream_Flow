import unittest
from scripts.load_remote_csv import load_remote_csv
import os

class TestLoadRemoteCSV(unittest.TestCase):
    def test_load_remote_csv(self):
        """
        Test the load_remote_csv function to ensure it downloads a CSV file.
        """
        try:
            load_remote_csv()
            self.assertTrue(os.path.exists("/tmp/remote_data.csv"))
        except Exception:
            self.fail("load_remote_csv failed unexpectedly")

if __name__ == "__main__":
    unittest.main()