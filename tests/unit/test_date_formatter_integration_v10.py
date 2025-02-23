import pytest
from src.utils.date_formatter import format_date

class TestDateFormatterIntegration:
    def test_format_date_integration(self):
        # Test the integration of format_date with various inputs
        assert format_date('2023-01-01') == 'January 1, 2023'
        assert format_date('2022-12-31') == 'December 31, 2022'
        assert format_date('invalid-date') == 'Invalid date format'

    def test_format_date_edge_cases(self):
        # Test edge cases for format_date function
        assert format_date('') == 'Invalid date format'
        assert format_date(None) == 'Invalid date format'