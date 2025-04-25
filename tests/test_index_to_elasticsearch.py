import unittest
import os
import json
from unittest.mock import patch, MagicMock
from scripts.index_to_elasticsearch import index_to_elasticsearch

class TestIndexToElasticsearch(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy directory with JSON files for testing Elasticsearch indexing.
        """
        # Create a dummy directory and JSON file
        os.makedirs("/tmp/kafka_output", exist_ok=True)
        sample_data = {"key": "value"}
        with open("/tmp/kafka_output/test.json", "w") as f:
            json.dump(sample_data, f)

    @patch('elasticsearch.Elasticsearch')  # Mock the Elasticsearch client
    def test_index_to_elasticsearch(self, mock_es):
        """
        Test the index_to_elasticsearch function to ensure it indexes data correctly.
        """
        # Create a mock Elasticsearch client
        mock_client = MagicMock()
        mock_es.return_value = mock_client
        
        # Run the function
        index_to_elasticsearch()
        
        # Verify that the Elasticsearch client was initialized
        mock_es.assert_called_once_with(['http://elasticsearch:9200'])
        
        # Verify that the data was indexed
        mock_client.index.assert_called_once_with(
            index="data_index",
            body={"key": "value"}
        )

if __name__ == "__main__":
    unittest.main()