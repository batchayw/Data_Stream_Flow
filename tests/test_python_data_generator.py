import unittest
import os
import json
from scripts.python_data_generator import python_data_generator

class TestPythonDataGenerator(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy CSV file for testing the data generator.
        """
        # Create a dummy CSV file with sample data
        with open("/tmp/spark_processed.csv", "w") as f:
            f.write("column_name\nvalue1\nvalue2\n")

    def test_python_data_generator(self):
        """
        Test the python_data_generator function to ensure it generates data and saves it as JSON.
        """
        # Run the data generator function
        python_data_generator()
        
        # Check if the output JSON file exists
        self.assertTrue(os.path.exists("/tmp/generated_data.json"))
        
        # Load the generated JSON and verify its content
        with open("/tmp/generated_data.json", "r") as f:
            data = json.load(f)
        
        # Verify the structure of the generated data
        self.assertEqual(len(data), 2)  # Should have 2 entries (value1, value2)
        self.assertIn("original_column", data[0])
        self.assertIn("generated_value", data[0])
        self.assertEqual(data[0]["original_column"], "value1")
        self.assertEqual(data[0]["generated_value"], "value1_generated")

if __name__ == "__main__":
    unittest.main()