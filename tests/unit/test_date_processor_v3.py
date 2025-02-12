import unittest
from src.utils.data_processor import process_data

class TestDataProcessorV3(unittest.TestCase):
    def test_valid_data(self):
        input_data = [1, 2, 3, 4, 5]
        expected_output = [1, 4, 9, 16, 25]
        self.assertEqual(process_data(input_data), expected_output)

    def test_empty_data(self):
        input_data = []
        expected_output = []
        self.assertEqual(process_data(input_data), expected_output)

    def test_invalid_data(self):
        input_data = [1, 'two', 3]
        with self.assertRaises(ValueError):
            process_data(input_data)

if __name__ == '__main__':
    unittest.main()