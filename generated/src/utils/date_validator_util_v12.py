# date_validator_util_v12.py

# This module contains utility functions for validating date formats.
# The functions ensure that the provided dates conform to specified formats,
# and handle exceptions gracefully.

from datetime import datetime

def is_valid_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Validate if the provided date string matches the expected format.

    Args:
        date_string (str): The date string to validate.
        date_format (str): The expected date format. Default is '%Y-%m-%d'.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def validate_dates(date_list: list, date_format: str = "%Y-%m-%d") -> list:
    """
    Validate a list of date strings and return a list of results.

    Args:
        date_list (list): List of date strings to validate.
        date_format (str): The expected date format. Default is '%Y-%m-%d'.

    Returns:
        list: List of tuples with date string and its validity.
    """
    return [(date, is_valid_date(date, date_format)) for date in date_list]
