import unittest
from src.utils.date_calculator import DateCalculator

class TestDateCalculator(unittest.TestCase):
    def setUp(self):
        self.date_calculator = DateCalculator()

    def test_add_days(self):
        result = self.date_calculator.add_days('2023-01-01', 10)
        self.assertEqual(result, '2023-01-11')

    def test_subtract_days(self):
        result = self.date_calculator.subtract_days('2023-01-11', 10)
        self.assertEqual(result, '2023-01-01')

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            self.date_calculator.add_days('invalid-date', 10)

if __name__ == '__main__':
    unittest.main()