# Date Validator Utility V7
# This module provides enhanced date validation functionalities.

from datetime import datetime

class DateValidator:
    """
    A class to validate various date formats.
    """

    @staticmethod
    def is_valid_date(date_string: str, date_format: str) -> bool:
        """
        Validate if the given date string matches the specified date format.
        
        Args:
            date_string (str): The date string to validate.
            date_format (str): The expected date format.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def validate_dates(dates: list, date_format: str) -> dict:
        """
        Validate a list of date strings against a given format.
        
        Args:
            dates (list): List of date strings to validate.
            date_format (str): The expected date format.
        
        Returns:
            dict: A dictionary with date strings as keys and validation results as values.
        """
        validation_results = {}
        for date in dates:
            validation_results[date] = DateValidator.is_valid_date(date, date_format)
        return validation_results

# Example usage
if __name__ == '__main__':
    dates_to_validate = ['2023-01-01', '2023-02-30', '2023-03-15']
    format_to_check = '%Y-%m-%d'
    results = DateValidator.validate_dates(dates_to_validate, format_to_check)
    print(results)  # Output will show which dates are valid or not.