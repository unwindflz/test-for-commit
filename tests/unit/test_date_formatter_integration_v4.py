import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatterIntegrationV4(unittest.TestCase):
    def setUp(self):
        self.formatter = DateFormatter()

    def test_integration_format_date(self):
        date_input = "2023-10-10"
        expected_output = "10th October 2023"
        self.assertEqual(self.formatter.format_date(date_input), expected_output)

    def test_integration_parse_date(self):
        date_input = "10th October 2023"
        expected_output = "2023-10-10"
        self.assertEqual(self.formatter.parse_date(date_input), expected_output)

if __name__ == '__main__':
    unittest.main()