import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatter(unittest.TestCase):
    def setUp(self):
        self.date_formatter = DateFormatter()

    def test_format_date_standard(self):
        formatted_date = self.date_formatter.format_date(datetime(2023, 1, 1), "%Y-%m-%d")
        self.assertEqual(formatted_date, "2023-01-01")

    def test_format_date_invalid(self):
        with self.assertRaises(ValueError):
            self.date_formatter.format_date("invalid date", "%Y-%m-%d")

    def test_format_date_edge_case(self):
        formatted_date = self.date_formatter.format_date(datetime(2023, 2, 29), "%Y-%m-%d")
        self.assertEqual(formatted_date, "2023-02-29")

    def test_format_date_empty(self):
        with self.assertRaises(ValueError):
            self.date_formatter.format_date(None, "%Y-%m-%d")

if __name__ == '__main__':
    unittest.main()