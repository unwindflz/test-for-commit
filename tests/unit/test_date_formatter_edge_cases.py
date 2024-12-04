import pytest
from src.utils.date_formatter import format_date

class TestDateFormatterEdgeCases:
    def test_empty_string(self):
        result = format_date("")
        assert result == "Invalid date"

    def test_invalid_date_format(self):
        result = format_date("2020-02-30")
        assert result == "Invalid date"

    def test_none_input(self):
        result = format_date(None)
        assert result == "Invalid date"

    def test_valid_date(self):
        result = format_date("2022-01-01")
        assert result == "January 1, 2022"  # Expected output format
