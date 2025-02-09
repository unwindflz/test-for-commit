import unittest
from src.utils.date_calculator import DateCalculator

class TestDateCalculator(unittest.TestCase):
    def test_add_days(self):
        result = DateCalculator.add_days('2023-01-01', 10)
        self.assertEqual(result, '2023-01-11')

    def test_subtract_days(self):
        result = DateCalculator.subtract_days('2023-01-10', 5)
        self.assertEqual(result, '2023-01-05')

    def test_calculate_difference(self):
        result = DateCalculator.calculate_difference('2023-01-01', '2023-01-10')
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()