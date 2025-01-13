import unittest

from src.utils.date_formatter import format_date

class TestDateFormatterIntegrationV3(unittest.TestCase):
    
    def test_format_date_integration(self):
        
        # Sample input and expected output
        input_date = '2023-10-01'
        expected_output = 'October 1, 2023'
        
        # Call the function
        result = format_date(input_date)
        
        # Assert the result
        self.assertEqual(result, expected_output)

    def test_format_date_invalid_input(self):
        
        # Sample invalid input
        input_date = 'invalid-date'
        
        # Call the function and assert it raises a ValueError
        with self.assertRaises(ValueError):
            format_date(input_date)

if __name__ == '__main__':
    unittest.main()