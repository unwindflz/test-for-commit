import pytest
from change_dates import modify_commit_dates

# Test cases for the commit date modification function

def test_modify_commit_date_valid():
    # Test modifying a valid commit date
    result = modify_commit_dates('2021-01-01', '2022-01-01')
    assert result == '2022-01-01', "Expected modified date to be '2022-01-01'"


def test_modify_commit_date_invalid_format():
    # Test modifying a date with an invalid format
    with pytest.raises(ValueError):
        modify_commit_dates('invalid-date', '2022-01-01')


def test_modify_commit_date_no_commit():
    # Test modifying date when no commit exists
    result = modify_commit_dates('2021-01-01', None)
    assert result is None, "Expected result to be None when no commit exists"


def test_modify_commit_date_edge_case():
    # Test edge case for date modification
    result = modify_commit_dates('2021-12-31', '2022-01-01')
    assert result == '2022-01-01', "Expected modified date to be '2022-01-01'"