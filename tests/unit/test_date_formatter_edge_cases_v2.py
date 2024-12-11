import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterEdgeCases(unittest.TestCase):
    def test_format_date_with_empty_input(self):
        self.assertIsNone(format_date(None))

    def test_format_date_with_invalid_format(self):
        with self.assertRaises(ValueError):
            format_date('invalid date', format='%Y-%m-%d')

    def test_format_date_with_leap_year(self):
        self.assertEqual(format_date('2020-02-29', format='%Y-%m-%d'), '2020-02-29')

    def test_format_date_with_nonexistent_date(self):
        with self.assertRaises(ValueError):
            format_date('2021-02-30', format='%Y-%m-%d')

if __name__ == '__main__':
    unittest.main()