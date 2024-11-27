import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterAdditional(unittest.TestCase):
    
    def test_format_date_with_invalid_input(self):
        # Test the output for invalid date inputs
        with self.assertRaises(ValueError):
            format_date('invalid-date')

    def test_format_date_edge_cases(self):
        # Test the output for edge case dates
        self.assertEqual(format_date('2023-01-01'), 'January 1, 2023')
        self.assertEqual(format_date('2023-12-31'), 'December 31, 2023')

if __name__ == '__main__':
    unittest.main()