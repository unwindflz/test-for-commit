import pytest
from src.utils.date_formatter import format_date


def test_format_date_valid():
    assert format_date('2023-01-01') == 'January 1, 2023'
    assert format_date('2020-07-15') == 'July 15, 2020'

def test_format_date_invalid():
    with pytest.raises(ValueError):
        format_date('invalid-date')
    with pytest.raises(ValueError):
        format_date('2020-02-30')  # Invalid date
