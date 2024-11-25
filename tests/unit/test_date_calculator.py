import unittest
from src.utils.date_calculator import add_days, subtract_days

class TestDateCalculator(unittest.TestCase):
    def test_add_days(self):
        self.assertEqual(add_days('2023-01-01', 5), '2023-01-06')
        self.assertEqual(add_days('2023-02-28', 1), '2023-03-01')

    def test_subtract_days(self):
        self.assertEqual(subtract_days('2023-01-06', 5), '2023-01-01')
        self.assertEqual(subtract_days('2023-03-01', 1), '2023-02-28')

if __name__ == '__main__':
    unittest.main()