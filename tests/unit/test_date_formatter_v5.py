import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterV5(unittest.TestCase):
    def test_format_date_standard(self):
        self.assertEqual(format_date('2023-01-01'), 'January 1, 2023')

    def test_format_date_edge_case(self):
        self.assertEqual(format_date('2023-02-29'), 'February 29, 2023')  # Leap year

    def test_format_date_invalid(self):
        with self.assertRaises(ValueError):
            format_date('invalid-date')

if __name__ == '__main__':
    unittest.main()