import unittest

from src.utils.date_formatter import DateFormatter

class TestDateFormatterIntegrationV6(unittest.TestCase):
    def test_format_date_integration(self):
        formatter = DateFormatter()
        input_date = "2023-01-01"
        expected_output = "January 1, 2023"
        self.assertEqual(formatter.format_date(input_date), expected_output)

    def test_format_date_invalid(self):
        formatter = DateFormatter()
        input_date = "invalid-date"
        with self.assertRaises(ValueError):
            formatter.format_date(input_date)

if __name__ == '__main__':
    unittest.main()