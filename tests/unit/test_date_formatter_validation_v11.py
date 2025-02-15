import pytest
from src.utils.date_formatter import validate_date_format


def test_valid_date_format():
    assert validate_date_format('2021-01-01') == True
    assert validate_date_format('01/01/2021') == True


def test_invalid_date_format():
    assert validate_date_format('2021/01/01') == False
    assert validate_date_format('01-01-2021') == False
    assert validate_date_format('2021-13-01') == False
    assert validate_date_format('2021-01-32') == False


@pytest.mark.parametrize("date_str, expected", [
    ('2021-01-01', True),
    ('2021-02-28', True),
    ('2021-02-29', False),  # Not a leap year
    ('2020-02-29', True),  # Leap year
])
def test_date_format_with_parametrize(date_str, expected):
    assert validate_date_format(date_str) == expected
