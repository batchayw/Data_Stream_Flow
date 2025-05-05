import unittest
import os
from unittest.mock import patch, MagicMock
from scripts.store_to_minio import store_to_minio

class TestStoreToMinIO(unittest.TestCase):
    def setUp(self):
        """
        Set up a dummy directory with JSON files for testing MinIO storage.
        """
        # Create a dummy directory and JSON file
        os.makedirs("/tmp/kafka_output", exist_ok=True)
        with open("/tmp/kafka_output/test.json", "w") as f:
            f.write('{"key": "value"}')

    @patch('scripts.store_to_minio.Minio')  # Patch Minio in the correct module
    def test_store_to_minio(self, mock_minio):
        """
        Test the store_to_minio function to ensure it uploads files to MinIO.
        """
        # Create a mock MinIO client
        mock_client = MagicMock()
        mock_minio.return_value = mock_client
        mock_client.bucket_exists.return_value = False
        
        # Run the function
        store_to_minio()
        
        # Verify that the MinIO client was initialized
        mock_minio.assert_called_once_with(
            "minio:9000",
            access_key="minioadmin",
            secret_key="minioadmin",
            secure=False
        )
        
        # Verify that the bucket was created
        mock_client.make_bucket.assert_called_once_with("data-bucket")
        
        # Verify that the file was uploaded
        mock_client.fput_object.assert_called_once_with(
            "data-bucket",
            "data/test.json",
            "/tmp/kafka_output/test.json"
        )

if __name__ == "__main__":
    unittest.main()