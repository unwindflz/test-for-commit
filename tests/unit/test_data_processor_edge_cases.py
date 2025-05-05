import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessorEdgeCases(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()

    def test_empty_input(self):
        """Test processing with empty input."""
        result = self.processor.process_data([])
        self.assertEqual(result, [], "Processing empty input should return an empty list.")

    def test_invalid_json_format(self):
        """Test processing with invalid JSON format."""
        invalid_json = '{invalid_json}'
        with self.assertRaises(ValueError):
            self.processor.process_data(invalid_json)

    def test_edge_case_large_numbers(self):
        """Test processing with very large numbers."""
        large_data = [{"value": 10**18}]
        result = self.processor.process_data(large_data)
        self.assertEqual(result[0]["value"], 10**18, "Processing large numbers should return the same number.")

    def test_edge_case_special_characters(self):
        """Test processing with special characters in strings."""
        special_char_data = [{"value": "!@#$%^&*()"}]
        result = self.processor.process_data(special_char_data)
        self.assertEqual(result[0]["value"], "!@#$%^&*()", "Special characters should be processed correctly.")

if __name__ == '__main__':
    unittest.main()