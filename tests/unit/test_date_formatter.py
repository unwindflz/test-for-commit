import unittest
from src.utils.date_formatter import format_date, parse_date

class TestDateFormatter(unittest.TestCase):

    def test_format_date(self):
        # Test formatting of a valid date
        self.assertEqual(format_date('2023-01-01'), 'January 1, 2023')
        self.assertEqual(format_date('2023-12-31'), 'December 31, 2023')

        # Test formatting of an invalid date
        with self.assertRaises(ValueError):
            format_date('invalid-date')

    def test_parse_date(self):
        # Test parsing of a valid date string
        self.assertEqual(parse_date('January 1, 2023'), '2023-01-01')
        self.assertEqual(parse_date('December 31, 2023'), '2023-12-31')

        # Test parsing of an invalid date string
        with self.assertRaises(ValueError):
            parse_date('invalid-date')

if __name__ == '__main__':
    unittest.main()