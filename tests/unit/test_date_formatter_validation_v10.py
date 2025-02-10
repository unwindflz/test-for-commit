import unittest
from src.utils.date_formatter import validate_date_format

class TestDateFormatterValidation(unittest.TestCase):

    def test_valid_date_format(self):
        self.assertTrue(validate_date_format('2023-10-01'))  # Valid format
        self.assertTrue(validate_date_format('01/10/2023'))  # Valid format

    def test_invalid_date_format(self):
        self.assertFalse(validate_date_format('2023-13-01'))  # Invalid month
        self.assertFalse(validate_date_format('2023-10-32'))  # Invalid day
        self.assertFalse(validate_date_format('not-a-date'))  # Completely invalid format

if __name__ == '__main__':
    unittest.main()