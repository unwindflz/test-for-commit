import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterIntegrationV9(unittest.TestCase):
    def test_format_date_integration(self):
        # Integration test for date formatting
        input_date = '2023-10-01'
        expected_output = 'October 1, 2023'
        result = format_date(input_date)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()