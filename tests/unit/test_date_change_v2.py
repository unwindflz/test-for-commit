import unittest
from src.models.date_change import DateChange

class TestDateChange(unittest.TestCase):
    def setUp(self):
        self.date_change = DateChange()

    def test_change_date_format(self):
        result = self.date_change.change_format('2023-10-01', '%d/%m/%Y')
        self.assertEqual(result, '01/10/2023')

    def test_change_date_timezone(self):
        result = self.date_change.change_timezone('2023-10-01T12:00:00Z', 'UTC', 'America/New_York')
        self.assertIn('2023-10-01', result)

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            self.date_change.change_format('invalid-date', '%d/%m/%Y')

if __name__ == '__main__':
    unittest.main()