import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessorIntegration(unittest.TestCase):
    """
    Integration tests for DataProcessor class, ensuring that
    data processing functionalities work as expected.
    """
    
    def setUp(self):
        """
        Set up the necessary environment for the tests.
        """
        self.processor = DataProcessor()

    def test_process_valid_data(self):
        """
        Test processing of valid data input.
        """
        input_data = {'key1': 'value1', 'key2': 'value2'}
        result = self.processor.process(input_data)
        expected_result = {'key1': 'VALUE1', 'key2': 'VALUE2'}  # Example transformation
        self.assertEqual(result, expected_result)

    def test_process_empty_data(self):
        """
        Test processing of empty data input.
        """
        input_data = {}
        result = self.processor.process(input_data)
        expected_result = {}  # Should return empty as well
        self.assertEqual(result, expected_result)

    def test_process_invalid_data(self):
        """
        Test handling of invalid data input.
        """
        input_data = None
        with self.assertRaises(ValueError):
            self.processor.process(input_data)

    def tearDown(self):
        """
        Clean up resources after tests.
        """
        self.processor = None

if __name__ == '__main__':
    unittest.main()