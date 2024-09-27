# date_validator_util_v10.py

"""
This module provides utility functions for validating dates.

Functions:
- is_valid_date(date_str: str, date_format: str) -> bool: Validates if the date string matches the given format.
"""

from datetime import datetime


def is_valid_date(date_str: str, date_format: str) -> bool:
    """
    Validate if the provided date string matches the expected format.

    Args:
        date_str (str): The date string to validate.
        date_format (str): The format to check against.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False
