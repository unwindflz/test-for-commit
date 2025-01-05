import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatterIntegration(unittest.TestCase):
    def test_format_date_integration(self):
        date_formatter = DateFormatter()
        result = date_formatter.format_date("2023-10-01")
        expected = "October 1, 2023"
        self.assertEqual(result, expected)

    def test_format_date_invalid_input(self):
        date_formatter = DateFormatter()
        with self.assertRaises(ValueError):
            date_formatter.format_date("invalid-date")

if __name__ == '__main__':
    unittest.main()