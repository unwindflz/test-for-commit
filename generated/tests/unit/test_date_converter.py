import unittest
from src.utils.date_converter import convert_date_format

class TestDateConverter(unittest.TestCase):

    def test_convert_date_format_valid(self):
        self.assertEqual(convert_date_format('2023-01-01', '%Y-%m-%d', '%d/%m/%Y'), '01/01/2023')
        self.assertEqual(convert_date_format('01-01-2023', '%d-%m-%Y', '%Y%m%d'), '20230101')

    def test_convert_date_format_invalid(self):
        with self.assertRaises(ValueError):
            convert_date_format('invalid-date', '%Y-%m-%d', '%d/%m/%Y')

    def test_convert_date_format_edge_cases(self):
        self.assertEqual(convert_date_format('2023-12-31', '%Y-%m-%d', '%d/%m/%Y'), '31/12/2023')
        self.assertEqual(convert_date_format('2020-02-29', '%Y-%m-%d', '%d/%m/%Y'), '29/02/2020')  # Leap year

if __name__ == '__main__':
    unittest.main()