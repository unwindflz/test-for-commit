import unittest
from src.utils.date_formatter import format_date

class TestDateFormatter(unittest.TestCase):
    def test_format_date(self):
        self.assertEqual(format_date('2023-01-01'), 'January 1, 2023')
        self.assertEqual(format_date('2022-12-31'), 'December 31, 2022')

if __name__ == '__main__':
    unittest.main()