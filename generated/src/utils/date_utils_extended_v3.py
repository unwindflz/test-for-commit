# date_utils_extended_v3.py

"""
Utility functions for date manipulation and formatting.

This module provides extended functionalities for various date-related operations.
"""

from datetime import datetime, timedelta


def add_days(start_date: str, days: int) -> str:
    """
    Add a specified number of days to a given date.

    Args:
        start_date (str): The date to which days will be added, in YYYY-MM-DD format.
        days (int): The number of days to add.

    Returns:
        str: The new date in YYYY-MM-DD format.
    """
    date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')


def format_date(date: str, input_format: str, output_format: str) -> str:
    """
    Convert a date from one format to another.

    Args:
        date (str): The date to convert.
        input_format (str): The format of the input date.
        output_format (str): The desired format for the output date.

    Returns:
        str: The date in the desired output format.
    """
    date_obj = datetime.strptime(date, input_format)
    return date_obj.strftime(output_format)


# Example usage
if __name__ == '__main__':
    print(add_days('2023-01-01', 10))  # Outputs: 2023-01-11
    print(format_date('01-11-2023', '%m-%d-%Y', '%Y/%m/%d'))  # Outputs: 2023/01/11