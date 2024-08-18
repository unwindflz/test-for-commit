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
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        return (end - start).days

    @staticmethod
    def add_days(date: str, days: int) -> str:
        """
        Add a number of days to a given date.
        :param date: The date in 'YYYY-MM-DD' format.
        :param days: The number of days to add.
        :return: The new date in 'YYYY-MM-DD' format.
        """
        original_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        new_date = original_date + datetime.timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

    @staticmethod
    def subtract_days(date: str, days: int) -> str:
        """
        Subtract a number of days from a given date.
        :param date: The date in 'YYYY-MM-DD' format.
        :param days: The number of days to subtract.
        :return: The new date in 'YYYY-MM-DD' format.
        """
        original_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        new_date = original_date - datetime.timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

# Example usage:
if __name__ == '__main__':
    print(DateCalculator.days_between('2023-01-01', '2023-01-10'))  # Output: 9
    print(DateCalculator.add_days('2023-01-01', 5))  # Output: 2023-01-06
    print(DateCalculator.subtract_days('2023-01-10', 3))  # Output: 2023-01-07
