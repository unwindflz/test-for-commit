import pytest
from src.utils.date_formatter import format_date

# Test cases for validating date formatting functionality

def test_format_date_valid_cases():
    assert format_date('2023-01-01') == 'January 1, 2023'
    assert format_date('2022-12-31') == 'December 31, 2022'
    assert format_date('2021-07-04') == 'July 4, 2021'


def test_format_date_invalid_cases():
    with pytest.raises(ValueError):
        format_date('invalid-date')
    with pytest.raises(ValueError):
        format_date('2022-02-30')  # Non-existent date


@pytest.mark.parametrize("date_input, expected_output", [
    ('2023-03-15', 'March 15, 2023'),
    ('2023-11-25', 'November 25, 2023'),
    ('2023-01-01', 'January 1, 2023')
])
def test_format_date_parametrized(date_input, expected_output):
    assert format_date(date_input) == expected_output
