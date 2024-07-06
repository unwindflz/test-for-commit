import datetime

class DateUtils:
    """
    A utility class for various date operations.
    """

    @staticmethod
    def get_current_date() -> str:
        """
        Get the current date in YYYY-MM-DD format.
        
        Returns:
            str: Current date as a string.
        """
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def days_between(start_date: str, end_date: str) -> int:
        """
        Calculate the number of days between two dates.
        
        Args:
            start_date (str): The start date in YYYY-MM-DD format.
            end_date (str): The end date in YYYY-MM-DD format.
        
        Returns:
            int: Number of days between the two dates.
            Raises ValueError if date format is incorrect.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            return (end - start).days
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

    @staticmethod
    def format_date(date: datetime.datetime, format_string: str) -> str:
        """
        Format a date into a specific string format.
        
        Args:
            date (datetime.datetime): The date to format.
            format_string (str): The format string.
        
        Returns:
            str: Formatted date string.
        """
        return date.strftime(format_string)