import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatterIntegrationV7(unittest.TestCase):
    def test_format_date(self):
        formatter = DateFormatter()
        self.assertEqual(formatter.format_date('2023-01-01'), 'January 1, 2023')

    def test_format_date_invalid(self):
        formatter = DateFormatter()
        with self.assertRaises(ValueError):
            formatter.format_date('invalid-date')

if __name__ == '__main__':
    unittest.main()