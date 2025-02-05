import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatterValidationV9(unittest.TestCase):
    
    def test_valid_date_format(self):
        formatter = DateFormatter()
        result = formatter.format_date("2023-10-01")  # Example valid date
        self.assertEqual(result, "October 1, 2023")

    def test_invalid_date_format(self):
        formatter = DateFormatter()
        with self.assertRaises(ValueError):
            formatter.format_date("invalid-date")  # Example invalid date

    def test_edge_case_empty_string(self):
        formatter = DateFormatter()
        with self.assertRaises(ValueError):
            formatter.format_date("")  # Edge case for empty string

    def test_edge_case_none(self):
        formatter = DateFormatter()
        with self.assertRaises(ValueError):
            formatter.format_date(None)  # Edge case for None

if __name__ == '__main__':
    unittest.main()