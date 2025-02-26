import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatterV10(unittest.TestCase):
    def test_format_date_standard(self):
        formatter = DateFormatter()
        formatted_date = formatter.format_date('2023-10-01')
        self.assertEqual(formatted_date, 'October 1, 2023')

    def test_format_date_invalid(self):
        formatter = DateFormatter()
        with self.assertRaises(ValueError):
            formatter.format_date('invalid-date')

    def test_format_date_edge_case(self):
        formatter = DateFormatter()
        formatted_date = formatter.format_date('2020-02-29')  # Leap year
        self.assertEqual(formatted_date, 'February 29, 2020')

if __name__ == '__main__':
    unittest.main()