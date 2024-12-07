import unittest
from src.utils.date_formatter import DateFormatter  

class TestDateFormatterV3(unittest.TestCase):
    def test_format_date_standard(self):
        formatter = DateFormatter()
        self.assertEqual(formatter.format_date('2023-10-01'), 'October 1, 2023')

    def test_format_date_edge_case(self):
        formatter = DateFormatter()
        self.assertEqual(formatter.format_date('2023-02-29'), 'February 29, 2023')  # Leap year check

    def test_format_invalid_date(self):
        formatter = DateFormatter()
        with self.assertRaises(ValueError):
            formatter.format_date('invalid-date')

if __name__ == '__main__':
    unittest.main()