import unittest
import json
import os
from unittest.mock import patch
from scripts.publish_to_kafka import publish_to_kafka

class TestPublishToKafka(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy JSON file for testing Kafka publishing.
        """
        # Create a dummy JSON file with sample data
        sample_data = [
            {"original_column": "value1", "generated_value": "value1_generated"},
            {"original_column": "value2", "generated_value": "value2_generated"}
        ]
        with open("/tmp/generated_data.json", "w") as f:
            json.dump(sample_data, f)

    @patch('kafka.KafkaProducer')  # Mock the KafkaProducer to avoid connecting to a real Kafka instance
    def test_publish_to_kafka(self, mock_producer):
        """
        Test the publish_to_kafka function to ensure it publishes data to Kafka.
        """
        # Create a mock producer instance
        mock_producer_instance = mock_producer.return_value
        
        # Run the function
        publish_to_kafka()
        
        # Verify that the producer was initialized with the correct bootstrap servers
        mock_producer.assert_called_once_with(
            bootstrap_servers=['kafka:9092'],
            value_serializer=mock_producer.call_args[1]['value_serializer']
        )
        
        # Verify that send was called for each record
        self.assertEqual(mock_producer_instance.send.call_count, 2)
        
        # Verify that flush and close were called
        mock_producer_instance.flush.assert_called_once()
        mock_producer_instance.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()