import unittest
from src.utils.date_converter import convert_date

class TestDateConverter(unittest.TestCase):
    def test_convert_date_valid(self):
        self.assertEqual(convert_date('2021-01-01', '%Y-%m-%d', '%d/%m/%Y'), '01/01/2021')
        self.assertEqual(convert_date('01/01/2021', '%d/%m/%Y', '%Y-%m-%d'), '2021-01-01')

    def test_convert_date_invalid(self):
        with self.assertRaises(ValueError):
            convert_date('invalid-date', '%Y-%m-%d', '%d/%m/%Y')

if __name__ == '__main__':
    unittest.main()