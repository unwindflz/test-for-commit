import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures for DataProcessor tests."""
        self.processor = DataProcessor()

    def test_process_valid_data(self):
        """Test processing of valid data inputs."""
        input_data = {'key1': 'value1', 'key2': 'value2'}
        expected_output = {'key1': 'value1', 'key2': 'value2', 'processed': True}
        self.assertEqual(self.processor.process(input_data), expected_output)

    def test_process_invalid_data(self):
        """Test processing of invalid data inputs raises exception."""
        input_data = None
        with self.assertRaises(ValueError):
            self.processor.process(input_data)

    def test_process_empty_data(self):
        """Test processing of empty data raises exception."""
        input_data = {}
        with self.assertRaises(ValueError):
            self.processor.process(input_data)

    def test_process_data_with_missing_keys(self):
        """Test processing of data missing required keys raises exception."""
        input_data = {'key1': 'value1'}
        with self.assertRaises(KeyError):
            self.processor.process(input_data)

if __name__ == '__main__':
    unittest.main()