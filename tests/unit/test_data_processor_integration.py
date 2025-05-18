import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessorIntegration(unittest.TestCase):
    """
    Integration tests for DataProcessor functionalities.
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        """  
        self.processor = DataProcessor()

    def test_process_valid_data(self):
        """
        Test processing of valid JSON data input.
        """  
        test_data = '{"key": "value"}'
        expected_output = {'key': 'value'}
        result = self.processor.process_data(test_data)
        self.assertEqual(result, expected_output)

    def test_process_invalid_data(self):
        """
        Test handling of invalid JSON data input.
        """  
        test_data = '{"key": "value"'
        with self.assertRaises(ValueError):
            self.processor.process_data(test_data)

    def test_process_empty_data(self):
        """
        Test processing of empty data input.
        """  
        test_data = ''
        with self.assertRaises(ValueError):
            self.processor.process_data(test_data)

    def tearDown(self):
        """
        Clean up after each test.
        """  
        self.processor = None

if __name__ == '__main__':
    unittest.main()