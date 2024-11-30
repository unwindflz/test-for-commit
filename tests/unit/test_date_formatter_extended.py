import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterExtended(unittest.TestCase):
    def test_format_date_with_custom_format(self):
        # Test formatting with a custom format
        date_input = '2023-10-01'
        expected_output = '01-10-2023'
        self.assertEqual(format_date(date_input, format='%d-%m-%Y'), expected_output)

    def test_format_date_with_invalid_date(self):
        # Test formatting with an invalid date input
        date_input = 'invalid-date'
        with self.assertRaises(ValueError):
            format_date(date_input)

    def test_format_date_default_format(self):
        # Test formatting with the default format
        date_input = '2023-10-01'
        expected_output = 'October 1, 2023'
        self.assertEqual(format_date(date_input), expected_output)

if __name__ == '__main__':
    unittest.main()