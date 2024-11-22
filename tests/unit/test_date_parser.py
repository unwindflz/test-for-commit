import unittest
from src.utils.date_parser import parse_date

class TestDateParser(unittest.TestCase):
    def test_valid_date(self):
        self.assertEqual(parse_date('2023-01-01'), '2023-01-01')
        self.assertEqual(parse_date('01/01/2023'), '2023-01-01')

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            parse_date('invalid-date')

    def test_leap_year(self):
        self.assertEqual(parse_date('2020-02-29'), '2020-02-29')
        with self.assertRaises(ValueError):
            parse_date('2019-02-29')

if __name__ == '__main__':
    unittest.main()