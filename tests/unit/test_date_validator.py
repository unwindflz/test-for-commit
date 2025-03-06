import unittest
from src.utils.date_validator import validate_date

class TestDateValidator(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(validate_date('2023-01-01'))  # YYYY-MM-DD format
        self.assertTrue(validate_date('2023/01/01'))  # YYYY/MM/DD format
        self.assertTrue(validate_date('01-01-2023'))  # DD-MM-YYYY format

    def test_invalid_date(self):
        self.assertFalse(validate_date('2023-02-30'))  # Invalid date
        self.assertFalse(validate_date('2023-13-01'))  # Invalid month
        self.assertFalse(validate_date('2023-00-01'))  # Invalid month
        self.assertFalse(validate_date('2023-01-32'))  # Invalid day

    def test_edge_cases(self):
        self.assertTrue(validate_date('2020-02-29'))  # Leap year
        self.assertFalse(validate_date('2019-02-29'))  # Not a leap year

if __name__ == '__main__':
    unittest.main()