# date_calculator_util_v4.py

"""
This module provides utility functions for date calculations,
including addition, subtraction, and formatting of dates.
"""

from datetime import datetime, timedelta


def add_days(start_date: str, days: int) -> str:
    """
    Add a specified number of days to a given date.

    Args:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        days (int): The number of days to add.

    Returns:
        str: The new date in 'YYYY-MM-DD' format.
    """
    date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def subtract_days(start_date: str, days: int) -> str:
    """
    Subtract a specified number of days from a given date.

    Args:
        start_date (str): The start date in 'YYYY-MM-DD' format.
        days (int): The number of days to subtract.

    Returns:
        str: The new date in 'YYYY-MM-DD' format.
    """
    date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date_obj - timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def format_date(date_str: str, format_str: str) -> str:
    """
    Format a date string to a specified format.

    Args:
        date_str (str): The date string to format.
        format_str (str): The format to apply.

    Returns:
        str: The formatted date string.
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime(format_str)