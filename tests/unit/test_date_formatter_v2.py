import unittest

from src.utils.date_formatter import format_date


class TestDateFormatter(unittest.TestCase):
    def test_format_date_valid(self):
        # Test with a valid date
        self.assertEqual(format_date('2023-10-01'), 'October 1, 2023')

    def test_format_date_invalid(self):
        # Test with an invalid date
        with self.assertRaises(ValueError):
            format_date('invalid-date')

    def test_format_date_empty(self):
        # Test with an empty string
        with self.assertRaises(ValueError):
            format_date('')


if __name__ == '__main__':
    unittest.main()