"""
Utility functions for date calculations.

This module provides various utility functions to perform calculations and manipulations on dates, including adding days, finding differences, and formatting.
"""

from datetime import datetime, timedelta


def add_days(start_date: str, days: int) -> str:
    """
    Add a specified number of days to a given date.
    
    Args:
        start_date (str): The date to which days will be added in YYYY-MM-DD format.
        days (int): The number of days to add.
    
    Returns:
        str: The new date after adding the days in YYYY-MM-DD format.
    """
    date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def days_between(date1: str, date2: str) -> int:
    """
    Calculate the number of days between two dates.
    
    Args:
        date1 (str): The first date in YYYY-MM-DD format.
        date2 (str): The second date in YYYY-MM-DD format.
    
    Returns:
        int: The number of days between the two dates.
    """
    date_obj1 = datetime.strptime(date1, '%Y-%m-%d')
    date_obj2 = datetime.strptime(date2, '%Y-%m-%d')
    delta = date_obj2 - date_obj1
    return delta.days


def format_date(date: str, format_str: str) -> str:
    """
    Format a given date string into a specified format.
    
    Args:
        date (str): The date to format in YYYY-MM-DD format.
        format_str (str): The desired format string.
    
    Returns:
        str: The formatted date string.
    """
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    return date_obj.strftime(format_str)
