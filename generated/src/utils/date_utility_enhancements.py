"""
Module for enhanced date utilities that support various operations on dates.
"""

from datetime import datetime, timedelta

class DateUtility:
    """
    A utility class for performing various date operations.
    """

    @staticmethod
    def add_days(original_date: str, days: int) -> str:
        """
        Adds a specified number of days to a given date.
        
        :param original_date: The original date in 'YYYY-MM-DD' format.
        :param days: Number of days to add.
        :return: New date in 'YYYY-MM-DD' format.
        """
        date_obj = datetime.strptime(original_date, '%Y-%m-%d')
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

    @staticmethod
    def subtract_days(original_date: str, days: int) -> str:
        """
        Subtracts a specified number of days from a given date.
        
        :param original_date: The original date in 'YYYY-MM-DD' format.
        :param days: Number of days to subtract.
        :return: New date in 'YYYY-MM-DD' format.
        """
        date_obj = datetime.strptime(original_date, '%Y-%m-%d')
        new_date = date_obj - timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """
        Checks if a given year is a leap year.
        
        :param year: The year to check.
        :return: True if leap year, False otherwise.
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage:
# print(DateUtility.add_days('2023-01-01', 10))  # Output: '2023-01-11'
# print(DateUtility.subtract_days('2023-01-11', 10))  # Output: '2023-01-01'
# print(DateUtility.is_leap_year(2024))  # Output: True
