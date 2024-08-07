import unittest
from src.utils.data_processor import DataProcessor


class TestDataProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = DataProcessor()

    def test_process_json_valid(self):
        json_data = '{"key": "value"}'
        expected = {'key': 'value'}
        result = self.processor.process_json(json_data)
        self.assertEqual(result, expected)

    def test_process_json_invalid(self):
        json_data = '{key: value}'  # Invalid JSON
        with self.assertRaises(ValueError):
            self.processor.process_json(json_data)

    def test_process_json_empty(self):
        json_data = ''
        with self.assertRaises(ValueError):
            self.processor.process_json(json_data)

    def test_process_file_valid(self):
        with open('test.json', 'w') as f:
            f.write('{"key": "value"}')
        expected = {'key': 'value'}
        result = self.processor.process_file('test.json')
        self.assertEqual(result, expected)

    def test_process_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            self.processor.process_file('non_existent.json')

    def tearDown(self):
        import os
        if os.path.exists('test.json'):
            os.remove('test.json')


if __name__ == '__main__':
    unittest.main()