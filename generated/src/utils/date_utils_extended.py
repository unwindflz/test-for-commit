# date_utils_extended.py

"""
This module contains extended utility functions for date manipulation.

The functions in this module are designed to work with date strings,
perform calculations, and convert between different date formats.
"""

from datetime import datetime, timedelta


def add_days(date_str, days):
    """
    Adds a specified number of days to a given date string.

    Parameters:
    date_str (str): The date string in 'YYYY-MM-DD' format.
    days (int): The number of days to add.

    Returns:
    str: The new date string in 'YYYY-MM-DD' format.
    """
    original_date = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = original_date + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def subtract_days(date_str, days):
    """
    Subtracts a specified number of days from a given date string.

    Parameters:
    date_str (str): The date string in 'YYYY-MM-DD' format.
    days (int): The number of days to subtract.

    Returns:
    str: The new date string in 'YYYY-MM-DD' format.
    """
    original_date = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = original_date - timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def format_date(date_str, current_format, desired_format):
    """
    Converts a date string from one format to another.

    Parameters:
    date_str (str): The date string to format.
    current_format (str): The current format of the date string.
    desired_format (str): The desired format to convert the date string to.

    Returns:
    str: The formatted date string.
    """
    date = datetime.strptime(date_str, current_format)
    return date.strftime(desired_format)