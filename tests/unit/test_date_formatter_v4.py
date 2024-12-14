import pytest
from src.utils.date_formatter import format_date


def test_format_date_standard():
    assert format_date('2023-01-01') == 'January 1, 2023'


def test_format_date_invalid():
    with pytest.raises(ValueError):
        format_date('invalid-date')


def test_format_date_edge_case():
    assert format_date('2023-02-29') == 'February 29, 2023'  # Leap year
