import unittest
from src.utils.date_calculator import DateCalculator

class TestDateCalculatorV2(unittest.TestCase):
    def test_add_days(self):
        self.assertEqual(DateCalculator.add_days('2022-01-01', 10), '2022-01-11')
        self.assertEqual(DateCalculator.add_days('2022-02-28', 1), '2022-03-01')

    def test_subtract_days(self):
        self.assertEqual(DateCalculator.subtract_days('2022-01-11', 10), '2022-01-01')
        self.assertEqual(DateCalculator.subtract_days('2022-03-01', 1), '2022-02-28')

    def test_edge_cases(self):
        self.assertEqual(DateCalculator.add_days('2022-01-31', 1), '2022-02-01')
        self.assertEqual(DateCalculator.subtract_days('2022-03-01', 29), '2022-02-01')

if __name__ == '__main__':
    unittest.main()