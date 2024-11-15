import unittest
from src.models.date_change import change_date

class TestDateChange(unittest.TestCase):
    def test_change_date_valid(self):
        result = change_date('2023-01-01', 5)
        self.assertEqual(result, '2023-01-06')  # Assuming change_date adds days correctly

    def test_change_date_invalid(self):
        with self.assertRaises(ValueError):
            change_date('invalid-date', 5)  # Should raise an error

if __name__ == '__main__':
    unittest.main()