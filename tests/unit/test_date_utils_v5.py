import unittest
from src.utils.date_utils import convert_date_format

class TestDateUtils(unittest.TestCase):
    def test_convert_date_format(self):
        # Test valid date conversion
        self.assertEqual(convert_date_format('2023-01-01', '%Y-%m-%d', '%d/%m/%Y'), '01/01/2023')
        # Test invalid input
        with self.assertRaises(ValueError):
            convert_date_format('invalid-date', '%Y-%m-%d', '%d/%m/%Y')
        # Test conversion with different formats
        self.assertEqual(convert_date_format('01/01/2023', '%d/%m/%Y', '%Y-%m-%d'), '2023-01-01')

if __name__ == '__main__':
    unittest.main()
