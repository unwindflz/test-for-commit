import datetime

class DateFormatter:
    """
    A utility class for formatting dates.
    """

    @staticmethod
    def format_date(date_obj):
        """
        Formats a given date object to a string in the format YYYY-MM-DD.
        
        Args:
            date_obj (datetime.date): The date object to format.
        
        Returns:
            str: The formatted date string.
        """
        if not isinstance(date_obj, datetime.date):
            raise ValueError('Input must be a datetime.date object.')
        return date_obj.strftime('%Y-%m-%d')

    @staticmethod
    def parse_date(date_string):
        """
        Parses a date string in the format YYYY-MM-DD to a date object.
        
        Args:
            date_string (str): The date string to parse.
        
        Returns:
            datetime.date: The parsed date object.
        """
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Input must be in YYYY-MM-DD format.')