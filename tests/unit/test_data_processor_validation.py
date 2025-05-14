import unittest
from src.utils.data_processor import DataProcessor

class TestDataProcessorValidation(unittest.TestCase):
    def setUp(self):
        """Set up the test case environment."""
        self.processor = DataProcessor()

    def test_valid_date_format(self):
        """Test valid date formats."""
        valid_dates = ["2023-10-05", "2023/10/05", "10-05-2023", "5th October 2023"]
        for date in valid_dates:
            self.assertTrue(self.processor.is_valid_date(date), f"{date} should be valid.")

    def test_invalid_date_format(self):
        """Test invalid date formats."""
        invalid_dates = ["2023-02-30", "2023/13/05", "10-05-23", "October 5th 2023"]
        for date in invalid_dates:
            self.assertFalse(self.processor.is_valid_date(date), f"{date} should be invalid.")

    def test_empty_date(self):
        """Test empty date input."""
        self.assertFalse(self.processor.is_valid_date(""), "Empty date should be invalid.")

    def test_none_date(self):
        """Test None date input."""
        self.assertFalse(self.processor.is_valid_date(None), "None should be invalid.")

if __name__ == '__main__':
    unittest.main()