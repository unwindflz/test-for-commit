import unittest
from src.utils.date_formatter import format_date

class TestDateFormatterV7(unittest.TestCase):
    def test_format_date_standard(self):
        self.assertEqual(format_date('2022-01-01'), 'January 1, 2022')

    def test_format_date_edge_case(self):
        self.assertEqual(format_date('2020-02-29'), 'February 29, 2020')
        self.assertEqual(format_date('2021-02-28'), 'February 28, 2021')

    def test_format_date_invalid(self):
        with self.assertRaises(ValueError):
            format_date('invalid-date')

if __name__ == '__main__':
    unittest.main()