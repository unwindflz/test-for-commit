import datetime

class DateConverter:
    """
    A utility class for converting dates between different formats.
    """

    @staticmethod
    def string_to_date(date_string: str, date_format: str) -> datetime.date:
        """
        Converts a date string to a datetime.date object.
        
        :param date_string: The date string to convert.
        :param date_format: The format of the input date string.
        :return: A datetime.date object.
        :raises ValueError: If the input string does not match the format.
        """
        try:
            return datetime.datetime.strptime(date_string, date_format).date()
        except ValueError as e:
            raise ValueError(f"Invalid date string '{date_string}' for format '{date_format}': {e}")

    @staticmethod
    def date_to_string(date: datetime.date, date_format: str) -> str:
        """
        Converts a datetime.date object to a formatted date string.
        
        :param date: The datetime.date object to convert.
        :param date_format: The format for the output date string.
        :return: A formatted date string.
        """
        return date.strftime(date_format)

    @staticmethod
    def iso_to_custom(date_string: str, custom_format: str) -> str:
        """
        Converts an ISO formatted date string to a custom formatted date string.
        
        :param date_string: The ISO formatted date string.
        :param custom_format: The desired output format.
        :return: A custom formatted date string.
        """
        date_obj = DateConverter.string_to_date(date_string, "%Y-%m-%d")
        return DateConverter.date_to_string(date_obj, custom_format)

    @staticmethod
    def custom_to_iso(date_string: str, custom_format: str) -> str:
        """
        Converts a custom formatted date string to an ISO formatted date string.
        
        :param date_string: The custom formatted date string.
        :param custom_format: The format of the input date string.
        :return: An ISO formatted date string.
        """
        date_obj = DateConverter.string_to_date(date_string, custom_format)
        return DateConverter.date_to_string(date_obj, "%Y-%m-%d")
