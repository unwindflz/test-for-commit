import unittest
from src.models.date_change import DateChange

class TestDateChange(unittest.TestCase):

    def test_date_change_valid(self):
        dc = DateChange("2023-01-01", "2023-01-02")
        self.assertEqual(dc.calculate_days_difference(), 1)

    def test_date_change_invalid_format(self):
        with self.assertRaises(ValueError):
            DateChange("2023-01-01", "InvalidDate")

    def test_date_change_negative_difference(self):
        dc = DateChange("2023-01-02", "2023-01-01")
        self.assertEqual(dc.calculate_days_difference(), -1)

if __name__ == '__main__':
    unittest.main()