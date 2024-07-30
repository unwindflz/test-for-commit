import re
from datetime import datetime

class DateParser:
    """
    A class for parsing date strings into datetime objects.
    """

    @staticmethod
    def parse_date(date_string: str) -> datetime:
        """
        Parses a date string in various formats and returns a datetime object.

        Args:
            date_string (str): The date string to parse.

        Returns:
            datetime: The parsed datetime object.

        Raises:
            ValueError: If the date string cannot be parsed.
        """
        # Define potential date formats
        formats = [
            "%Y-%m-%d",
            "%d/%m/%Y",
            "%m-%d-%Y",
            "%B %d, %Y",
            "%d %B %Y"
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_string, fmt)
            except ValueError:
                continue  # Try the next format
        raise ValueError(f"Date '{date_string}' is not in a recognized format.")

    @staticmethod
    def is_valid_date(date_string: str) -> bool:
        """
        Checks if the given date string is valid according to the recognized formats.

        Args:
            date_string (str): The date string to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            DateParser.parse_date(date_string)
            return True
        except ValueError:
            return False

# Example usage:
if __name__ == '__main__':
    test_date = "2023-10-05"
    if DateParser.is_valid_date(test_date):
        parsed_date = DateParser.parse_date(test_date)
        print(f"Parsed date: {parsed_date}")
    else:
        print(f"Invalid date format for: {test_date}")
