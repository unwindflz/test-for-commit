import unittest
from src.utils.date_formatter import DateFormatter

class TestDateFormatter(unittest.TestCase):

    def setUp(self):
        """Create a DateFormatter instance for testing."""
        self.date_formatter = DateFormatter()

    def test_format_date_standard(self):
        """Test formatting a standard date."""
        date = datetime.datetime(2021, 1, 1)
        formatted = self.date_formatter.format_date(date)
        self.assertEqual(formatted, '2021-01-01')

    def test_format_date_invalid(self):
        """Test formatting an invalid date raises error."""
        with self.assertRaises(ValueError):
            self.date_formatter.format_date('invalid-date')

    def test_format_date_edge_case(self):
        """Test formatting a date on a leap year."""
        date = datetime.datetime(2020, 2, 29)
        formatted = self.date_formatter.format_date(date)
        self.assertEqual(formatted, '2020-02-29')

    def test_format_date_none(self):
        """Test formatting None raises error."""
        with self.assertRaises(TypeError):
            self.date_formatter.format_date(None)

if __name__ == '__main__':
    unittest.main()