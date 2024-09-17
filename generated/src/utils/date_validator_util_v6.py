# date_validator_util_v6.py

"""Utility functions for date validation.

This module contains enhanced functions to validate dates,
ensuring they meet specific criteria and formats.
"""

import re
from datetime import datetime

def is_valid_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """Check if the provided date string is valid.

    Args:
        date_string (str): The date string to validate.
        date_format (str): The format against which to validate.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False

def is_date_in_past(date_string: str) -> bool:
    """Check if the provided date string is in the past.

    Args:
        date_string (str): The date string to check.

    Returns:
        bool: True if the date is in the past, False otherwise.
    """
    date_format = "%Y-%m-%d"
    if is_valid_date(date_string, date_format):
        return datetime.strptime(date_string, date_format) < datetime.now()
    return False

# Additional utility functions can be added here to extend
# the functionality of date validation.
