# date_validator_util_v4.py

"""
Utility functions for validating date formats.

This module contains functions to validate whether a given string is a valid date format.
"""

from datetime import datetime


def is_valid_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Check if the provided date string matches the given date format.

    Args:
        date_string (str): The date string to validate.
        date_format (str): The format to validate against (default is '%Y-%m-%d').

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def validate_dates(date_list: list, date_format: str = "%Y-%m-%d") -> list:
    """
    Validate a list of date strings against the specified format.

    Args:
        date_list (list): A list of date strings to validate.
        date_format (str): The format to validate against (default is '%Y-%m-%d').

    Returns:
        list: A list of invalid date strings.
    """
    invalid_dates = []
    for date in date_list:
        if not is_valid_date(date, date_format):
            invalid_dates.append(date)
    return invalid_dates
