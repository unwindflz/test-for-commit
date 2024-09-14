# date_validator_util_v5.py

"""
This module provides utility functions for validating date formats.

Functions:
- is_valid_date(date_str, date_format): Check if the date string matches the specified format.
- is_leap_year(year): Determine if a given year is a leap year.
"""

from datetime import datetime


def is_valid_date(date_str, date_format="%Y-%m-%d"):
    """
    Validate if the given date string matches the specified format.
    
    Args:
        date_str (str): The date string to validate.
        date_format (str): The format to validate against (default: '%Y-%m-%d').
    
    Returns:
        bool: True if the date matches the format, False otherwise.
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def is_leap_year(year):
    """
    Check if the specified year is a leap year.
    
    Args:
        year (int): The year to check.
    
    Returns:
        bool: True if it's a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)