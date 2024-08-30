import datetime

class DateFormatterUtil:
    """
    A utility class for formatting dates in various ways.
    """

    @staticmethod
    def format_date(date: datetime.date, format_string: str) -> str:
        """
        Format a given date using the specified format string.
        
        Args:
            date (datetime.date): The date to format.
            format_string (str): The format string, e.g., '%Y-%m-%d'.

        Returns:
            str: The formatted date as a string.
        """
        return date.strftime(format_string)

    @staticmethod
    def parse_date(date_string: str, format_string: str) -> datetime.date:
        """
        Parse a date string into a datetime.date object based on the format string.
        
        Args:
            date_string (str): The date string to parse.
            format_string (str): The format string, e.g., '%Y-%m-%d'.

        Returns:
            datetime.date: The parsed date.

        Raises:
            ValueError: If the date_string does not match the format_string.
        """
        return datetime.datetime.strptime(date_string, format_string).date()

    @staticmethod
    def get_today() -> datetime.date:
        """
        Returns the current date.
        
        Returns:
            datetime.date: Today's date.
        """
        return datetime.date.today()