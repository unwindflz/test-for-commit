import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessorUsage(unittest.TestCase):
    """
    Unit tests for the DataProcessor class functionality.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        self.processor = DataProcessor()

    def test_process_valid_data(self):
        """
        Test processing of valid data.
        """
        valid_data = {'key1': 'value1', 'key2': 'value2'}
        result = self.processor.process_data(valid_data)
        self.assertIsNotNone(result)
        self.assertEqual(result['key1'], 'value1')

    def test_process_invalid_data(self):
        """
        Test processing of invalid data raises exception.
        """
        invalid_data = None
        with self.assertRaises(ValueError):
            self.processor.process_data(invalid_data)

    def test_process_empty_data(self):
        """
        Test processing of empty data raises exception.
        """
        empty_data = {}
        with self.assertRaises(ValueError):
            self.processor.process_data(empty_data)

    def test_process_data_with_missing_keys(self):
        """
        Test processing of data with missing keys raises exception.
        """
        missing_keys_data = {'key1': 'value1'}  # Missing key2
        with self.assertRaises(KeyError):
            self.processor.process_data(missing_keys_data)


if __name__ == '__main__':
    unittest.main()