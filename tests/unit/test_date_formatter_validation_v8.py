import pytest
from src.utils.date_formatter import DateFormatter


def test_date_formatter_valid_dates():
    formatter = DateFormatter()
    assert formatter.format_date("2023-10-01") == "October 1, 2023"
    assert formatter.format_date("2022-01-15") == "January 15, 2022"


def test_date_formatter_invalid_dates():
    formatter = DateFormatter()
    with pytest.raises(ValueError):
        formatter.format_date("invalid-date")
    with pytest.raises(ValueError):
        formatter.format_date("2023-02-30")  # Invalid date


def test_date_formatter_edge_cases():
    formatter = DateFormatter()
    assert formatter.format_date("2020-02-29") == "February 29, 2020"  # Leap year
    assert formatter.format_date("1970-01-01") == "January 1, 1970"  # Unix epoch