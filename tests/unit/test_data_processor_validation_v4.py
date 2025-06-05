import unittest
from src.utils.data_processor import DataProcessor


class TestDataProcessorValidationV4(unittest.TestCase):
    """
    Unit tests for the validation logic in DataProcessor version 4.
    """

    def setUp(self):
        """
        Set up the DataProcessor instance for testing.
        """
        self.processor = DataProcessor()

    def test_valid_date_format(self):
        """
        Test that valid date formats are accepted.
        """
        valid_dates = [
            "2023-01-01",
            "01/01/2023",
            "January 1, 2023"
        ]
        for date in valid_dates:
            self.assertTrue(self.processor.validate_date_format(date))

    def test_invalid_date_format(self):
        """
        Test that invalid date formats are rejected.
        """
        invalid_dates = [
            "2023-13-01",
            "2023-02-30",
            "01/2023/01",
            "Invalid Date"
        ]
        for date in invalid_dates:
            self.assertFalse(self.processor.validate_date_format(date))

    def test_edge_case_dates(self):
        """
        Test the edge cases for date validation.
        """
        edge_dates = [
            "2020-02-29",  # Leap year
            "2021-02-29",  # Not a leap year
            "2023-12-31"   # End of year
        ]
        self.assertTrue(self.processor.validate_date_format(edge_dates[0]))
        self.assertFalse(self.processor.validate_date_format(edge_dates[1]))
        self.assertTrue(self.processor.validate_date_format(edge_dates[2]))


if __name__ == '__main__':
    unittest.main()