import unittest
from src.utils.data_processor import process_data

class TestDataProcessor(unittest.TestCase):
    def test_process_data_valid(self):
        input_data = [1, 2, 3]
        expected_output = [2, 4, 6]  # Assuming process_data doubles the input
        result = process_data(input_data)
        self.assertEqual(result, expected_output)

    def test_process_data_empty(self):
        input_data = []
        expected_output = []
        result = process_data(input_data)
        self.assertEqual(result, expected_output)

    def test_process_data_invalid(self):
        input_data = [1, 'two', 3]
        with self.assertRaises(TypeError):
            process_data(input_data)

if __name__ == '__main__':
    unittest.main()