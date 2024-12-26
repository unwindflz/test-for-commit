import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterIntegration(unittest.TestCase):
    def test_format_date_integration(self):
        # Test formatting a date string
        date_string = '2023-10-01'
        expected_output = 'October 1, 2023'
        result = format_date(date_string)
        self.assertEqual(result, expected_output)

    def test_format_date_invalid(self):
        # Test formatting an invalid date string
        date_string = 'invalid-date'
        with self.assertRaises(ValueError):
            format_date(date_string)

if __name__ == '__main__':
    unittest.main()