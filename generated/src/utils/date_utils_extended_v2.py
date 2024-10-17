"""
This module provides extended utilities for date manipulations.

Functions:
- add_days(date, days): Returns a new date that is the given number of days after the provided date.
- subtract_days(date, days): Returns a new date that is the given number of days before the provided date.
- format_date(date, format_string): Returns the date formatted as per the provided format string.
"""

from datetime import datetime, timedelta


def add_days(date, days):
    """
    Adds a specified number of days to a given date.
    
    :param date: The original date (datetime object).
    :param days: Number of days to add (int).
    :return: New date after adding days (datetime object).
    """
    return date + timedelta(days=days)


def subtract_days(date, days):
    """
    Subtracts a specified number of days from a given date.
    
    :param date: The original date (datetime object).
    :param days: Number of days to subtract (int).
    :return: New date after subtracting days (datetime object).
    """
    return date - timedelta(days=days)


def format_date(date, format_string):
    """
    Formats a date according to the specified format string.
    
    :param date: The date to format (datetime object).
    :param format_string: The format string (str).
    :return: Formatted date as string.
    """
    return date.strftime(format_string)