import unittest
from src.utils.date_calculator import calculate_date_difference, is_leap_year

class TestDateCalculator(unittest.TestCase):

    def test_calculate_date_difference(self):
        self.assertEqual(calculate_date_difference('2023-01-01', '2023-01-02'), 1)
        self.assertEqual(calculate_date_difference('2023-01-01', '2023-01-01'), 0)
        self.assertEqual(calculate_date_difference('2023-01-01', '2023-02-01'), 31)

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2020))  # 2020 is a leap year
        self.assertFalse(is_leap_year(2021))  # 2021 is not a leap year
        self.assertTrue(is_leap_year(2000))  # 2000 is a leap year
        self.assertFalse(is_leap_year(1900))  # 1900 is not a leap year

if __name__ == '__main__':
    unittest.main()