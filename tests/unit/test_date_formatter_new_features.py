import pytest
from src.utils.date_formatter import format_date, parse_date

class TestDateFormatter:
    def test_format_date(self):
        assert format_date("2023-10-01") == "October 1, 2023"
        assert format_date("2023-02-15") == "February 15, 2023"

    def test_parse_date(self):
        assert parse_date("October 1, 2023") == "2023-10-01"
        assert parse_date("February 15, 2023") == "2023-02-15"

    def test_format_date_invalid(self):
        with pytest.raises(ValueError):
            format_date("invalid-date")

    def test_parse_date_invalid(self):
        with pytest.raises(ValueError):
            parse_date("invalid-date")
