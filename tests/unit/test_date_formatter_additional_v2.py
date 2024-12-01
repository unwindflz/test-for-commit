import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterAdditional(unittest.TestCase):
    def test_format_date_standard(self):
        self.assertEqual(format_date('2023-01-01'), 'January 1, 2023')

    def test_format_date_empty_string(self):
        with self.assertRaises(ValueError):
            format_date('')

    def test_format_date_invalid(self):
        with self.assertRaises(ValueError):
            format_date('invalid-date')

if __name__ == '__main__':
    unittest.main()