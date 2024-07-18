import datetime

class DateCalculator:
    """
    A utility class for performing calculations on dates.
    """

    @staticmethod
    def add_days(start_date: datetime.date, days: int) -> datetime.date:
        """
        Adds a specified number of days to a given date.
        
        :param start_date: The date to which days will be added.
        :param days: The number of days to add.
        :return: A new date after adding the specified days.
        """
        return start_date + datetime.timedelta(days=days)

    @staticmethod
    def subtract_days(start_date: datetime.date, days: int) -> datetime.date:
        """
        Subtracts a specified number of days from a given date.
        
        :param start_date: The date from which days will be subtracted.
        :param days: The number of days to subtract.
        :return: A new date after subtracting the specified days.
        """
        return start_date - datetime.timedelta(days=days)

    @staticmethod
    def days_between(date1: datetime.date, date2: datetime.date) -> int:
        """
        Calculates the number of days between two dates.
        
        :param date1: The first date.
        :param date2: The second date.
        :return: The number of days between the two dates.
        """
        delta = date2 - date1
        return delta.days
