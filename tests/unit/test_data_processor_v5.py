import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessorV5(unittest.TestCase):
    """
    Unit tests for version 5 of the DataProcessor class.
    """

    def setUp(self):
        """
        Set up the test case for DataProcessor V5.
        """
        self.processor = DataProcessor(version=5)

    def test_process_valid_data(self):
        """
        Test processing of valid data.
        """
        input_data = {'key': 'value'}
        expected_output = {'processed_key': 'processed_value'}  # Expected output after processing
        output = self.processor.process(input_data)
        self.assertEqual(output, expected_output)

    def test_process_invalid_data(self):
        """
        Test processing of invalid data to ensure error is raised.
        """
        input_data = {'invalid_key': 'value'}
        with self.assertRaises(ValueError):
            self.processor.process(input_data)

    def test_version_check(self):
        """
        Test to ensure version is set correctly.
        """
        self.assertEqual(self.processor.version, 5)

    def test_data_format(self):
        """
        Test to ensure output data format is as expected.
        """
        input_data = {'key': 'value'}
        output = self.processor.process(input_data)
        self.assertIsInstance(output, dict)

if __name__ == '__main__':
    unittest.main()