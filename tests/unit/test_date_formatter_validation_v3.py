import pytest
from src.utils.date_formatter import DateFormatter


def test_date_formatter_valid_cases():
    formatter = DateFormatter()
    assert formatter.format('2023-01-01') == 'January 1, 2023'
    assert formatter.format('2023-12-31') == 'December 31, 2023'


def test_date_formatter_invalid_cases():
    formatter = DateFormatter()
    with pytest.raises(ValueError):
        formatter.format('not-a-date')
    with pytest.raises(ValueError):
        formatter.format('2023-02-30')  # Invalid date


@pytest.mark.parametrize('date_input, expected_output', [
    ('2023-01-01', 'January 1, 2023'),
    ('2023-12-31', 'December 31, 2023'),
])
def test_date_formatter_parametrized(date_input, expected_output):
    formatter = DateFormatter()
    assert formatter.format(date_input) == expected_output
