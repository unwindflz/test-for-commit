import unittest
from src.utils.date_calculator import add_days, subtract_days

class TestDateCalculator(unittest.TestCase):
    
    def test_add_days(self):
        self.assertEqual(add_days('2023-01-01', 10), '2023-01-11')
        self.assertEqual(add_days('2023-02-28', 1), '2023-03-01')
        self.assertEqual(add_days('2023-12-31', 1), '2024-01-01')
        self.assertEqual(add_days('2023-01-01', -10), '2022-12-22')

    def test_subtract_days(self):
        self.assertEqual(subtract_days('2023-01-11', 10), '2023-01-01')
        self.assertEqual(subtract_days('2023-03-01', 1), '2023-02-28')
        self.assertEqual(subtract_days('2024-01-01', 1), '2023-12-31')
        self.assertEqual(subtract_days('2023-01-01', -10), '2023-01-11')

if __name__ == '__main__':
    unittest.main()