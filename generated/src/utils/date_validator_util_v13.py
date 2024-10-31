# date_validator_util_v13.py

"""
Utility functions for validating date formats and ensuring they meet specific criteria.

This module provides functions to validate various date formats and check for valid date ranges.
"""

from datetime import datetime
from typing import Optional


def is_valid_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Validate if the provided date_string matches the expected date_format.
    
    Args:
        date_string (str): The date string to validate.
        date_format (str): The format that the date_string should match.
    
    Returns:
        bool: True if the date_string is valid, False otherwise.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def is_date_in_range(date_string: str, start_date: str, end_date: str, date_format: str = "%Y-%m-%d") -> bool:
    """
    Check if the given date_string falls within the specified date range.
    
    Args:
        date_string (str): The date string to check.
        start_date (str): The start date of the range.
        end_date (str): The end date of the range.
        date_format (str): The format that the dates should match.
    
    Returns:
        bool: True if date_string is within the range, False otherwise.
    """
    if not (is_valid_date(date_string, date_format) and 
            is_valid_date(start_date, date_format) and 
            is_valid_date(end_date, date_format)):
        return False
    date = datetime.strptime(date_string, date_format)
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    return start <= date <= end
