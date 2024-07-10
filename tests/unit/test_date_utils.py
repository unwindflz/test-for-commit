import unittest
from src.utils.date_utils import DateUtils

class TestDateUtils(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(DateUtils.is_valid_date('2023-01-01'))
        self.assertTrue(DateUtils.is_valid_date('2020-02-29'))  # Leap year

    def test_invalid_date(self):
        self.assertFalse(DateUtils.is_valid_date('2023-02-30'))
        self.assertFalse(DateUtils.is_valid_date('2023-13-01'))
        self.assertFalse(DateUtils.is_valid_date('2023-00-01'))
        self.assertFalse(DateUtils.is_valid_date('invalid-date'))

    def test_date_formatting(self):
        self.assertEqual(DateUtils.format_date('2023-01-01'), 'January 1, 2023')
        self.assertEqual(DateUtils.format_date('2023-12-31'), 'December 31, 2023')

    def test_edge_cases(self):
        self.assertTrue(DateUtils.is_valid_date('2023-12-31'))
        self.assertFalse(DateUtils.is_valid_date('2023-11-31'))  # Invalid day

if __name__ == '__main__':
    unittest.main()