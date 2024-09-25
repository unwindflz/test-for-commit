# date_validator_util_v9.py

"""
Utility functions for validating date formats, ensuring that the dates are in the correct format and within acceptable ranges.

This module contains various validation functions that can be reused across the application.
"""

from datetime import datetime


def is_valid_date_format(date_string, date_format='%Y-%m-%d'):
    """
    Validate if the given date string matches the specified format.
    
    Args:
        date_string (str): The date string to validate.
        date_format (str): The format to validate against (default is '%Y-%m-%d').
    
    Returns:
        bool: True if valid format, False otherwise.
    """
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def is_date_in_range(date_string, start_date, end_date, date_format='%Y-%m-%d'):
    """
    Check if the date_string falls within the specified range.
    
    Args:
        date_string (str): The date string to validate.
        start_date (str): The start date in the specified format.
        end_date (str): The end date in the specified format.
        date_format (str): The format to validate against (default is '%Y-%m-%d').
    
    Returns:
        bool: True if the date is within the range, False otherwise.
    """
    if not is_valid_date_format(date_string, date_format):
        return False
    date_to_check = datetime.strptime(date_string, date_format)
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    return start <= date_to_check <= end
