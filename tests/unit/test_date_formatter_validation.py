import pytest
from src.utils.date_formatter import format_date


def test_format_date_valid():
    assert format_date('2023-10-01') == 'October 1, 2023'
    assert format_date('2023-12-25') == 'December 25, 2023'


def test_format_date_invalid():
    with pytest.raises(ValueError):
        format_date('invalid-date-string')
    with pytest.raises(ValueError):
        format_date('2023-02-30')  # Invalid date
