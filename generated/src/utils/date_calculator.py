import datetime

class DateCalculator:
    """
    A utility class for performing calculations on dates.
    """

    @staticmethod
    def days_between(start_date: str, end_date: str) -> int:
        """
        Calculate the number of days between two dates.
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param end_date: The end date in 'YYYY-MM-DD' format.
        :return: The number of days between the two dates.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            delta = end - start
            return delta.days
        except ValueError as e:
            print(f'Error parsing dates: {e}')
            return 0

    @staticmethod
    def add_days(start_date: str, days: int) -> str:
        """
        Add a specified number of days to a given date.
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param days: The number of days to add.
        :return: The new date in 'YYYY-MM-DD' format.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            new_date = start + datetime.timedelta(days=days)
            return new_date.strftime('%Y-%m-%d')
        except ValueError as e:
            print(f'Error parsing date: {e}')
            return ''

    @staticmethod
    def subtract_days(start_date: str, days: int) -> str:
        """
        Subtract a specified number of days from a given date.
        :param start_date: The start date in 'YYYY-MM-DD' format.
        :param days: The number of days to subtract.
        :return: The new date in 'YYYY-MM-DD' format.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            new_date = start - datetime.timedelta(days=days)
            return new_date.strftime('%Y-%m-%d')
        except ValueError as e:
            print(f'Error parsing date: {e}')
            return ''
