# date_validator_util_v11.py

"""
Utility functions for validating dates.

This module provides various functions to validate date formats and check the validity of given dates.
"""

from datetime import datetime


def is_valid_date(date_str, date_format="%Y-%m-%d"):
    """
    Validate a date string against a specified format.

    Args:
        date_str (str): The date string to validate.
        date_format (str): The format to validate against (default is '%Y-%m-%d').

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def is_date_in_past(date_str, date_format="%Y-%m-%d"):
    """
    Check if the given date is in the past.

    Args:
        date_str (str): The date string to check.
        date_format (str): The format to validate against (default is '%Y-%m-%d').

    Returns:
        bool: True if the date is in the past, False otherwise.
    """
    if is_valid_date(date_str, date_format):
        return datetime.strptime(date_str, date_format) < datetime.now()
    return False


def is_date_in_future(date_str, date_format="%Y-%m-%d"):
    """
    Check if the given date is in the future.

    Args:
        date_str (str): The date string to check.
        date_format (str): The format to validate against (default is '%Y-%m-%d').

    Returns:
        bool: True if the date is in the future, False otherwise.
    """
    if is_valid_date(date_str, date_format):
        return datetime.strptime(date_str, date_format) > datetime.now()
    return False

