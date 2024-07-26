import re

class DateValidator:
    """
    A utility class for validating date strings.
    """

    @staticmethod
    def is_valid_date(date_string: str) -> bool:
        """
        Checks if the provided date string is in the format YYYY-MM-DD.
        :param date_string: The date string to validate.
        :return: True if valid, False otherwise.
        """
        date_pattern = r'^(\d{4})-(\d{2})-(\d{2})$'
        if re.match(date_pattern, date_string):
            return True
        return False

    @staticmethod
    def is_valid_date_range(start_date: str, end_date: str) -> bool:
        """
        Checks if the provided start and end date strings are valid and if
        the start date is before the end date.
        :param start_date: The start date string.
        :param end_date: The end date string.
        :return: True if valid range, False otherwise.
        """
        if not (DateValidator.is_valid_date(start_date) and DateValidator.is_valid_date(end_date)):
            return False
        return start_date < end_date
