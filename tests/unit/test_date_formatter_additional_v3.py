import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatterAdditionalV3(unittest.TestCase):
    def test_format_date_with_timezone(self):
        date_str = '2023-10-01T12:00:00Z'
        expected_output = '01 Oct 2023 12:00 PM UTC'
        result = DateFormatter.format_date(date_str, '%d %b %Y %I:%M %p %Z')
        self.assertEqual(result, expected_output)

    def test_format_invalid_date(self):
        date_str = 'invalid-date'
        with self.assertRaises(ValueError):
            DateFormatter.format_date(date_str, '%d %b %Y')

if __name__ == '__main__':
    unittest.main()