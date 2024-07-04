import datetime

class DateParser:
    """
    A utility class for parsing and validating dates.
    """

    @staticmethod
    def parse_date(date_string: str, date_format: str = "%Y-%m-%d") -> datetime.date:
        """
        Parses a date string into a datetime.date object.
        
        :param date_string: The date string to parse.
        :param date_format: The format of the date string (default is '%Y-%m-%d').
        :return: A datetime.date object if parsing is successful.
        :raises ValueError: If the date string is invalid.
        """
        try:
            parsed_date = datetime.datetime.strptime(date_string, date_format).date()
            return parsed_date
        except ValueError as e:
            raise ValueError(f"Invalid date: '{date_string}'. Expected format: '{date_format}'.") from e

    @staticmethod
    def is_valid_date(date_string: str, date_format: str = "%Y-%m-%d") -> bool:
        """
        Validates if a date string matches the given format.
        
        :param date_string: The date string to validate.
        :param date_format: The format of the date string (default is '%Y-%m-%d').
        :return: True if valid, False otherwise.
        """
        try:
            datetime.datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
