import datetime

class DateCalculator:
    """
    A class for performing various date calculations.
    """

    @staticmethod
    def days_between(start_date: str, end_date: str) -> int:
        """
        Calculate the number of days between two dates.

        Args:
            start_date (str): The start date in 'YYYY-MM-DD' format.
            end_date (str): The end date in 'YYYY-MM-DD' format.

        Returns:
            int: The number of days between the two dates.

        Raises:
            ValueError: If the date format is incorrect.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
            return (end - start).days
        except ValueError as e:
            raise ValueError(f"Incorrect date format: {e}")

    @staticmethod
    def add_days(start_date: str, days: int) -> str:
        """
        Add a specific number of days to a given date.

        Args:
            start_date (str): The starting date in 'YYYY-MM-DD' format.
            days (int): The number of days to add.

        Returns:
            str: The new date after adding the days in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the date format is incorrect.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            new_date = start + datetime.timedelta(days=days)
            return new_date.strftime('%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Incorrect date format: {e}")

    @staticmethod
    def subtract_days(start_date: str, days: int) -> str:
        """
        Subtract a specific number of days from a given date.

        Args:
            start_date (str): The starting date in 'YYYY-MM-DD' format.
            days (int): The number of days to subtract.

        Returns:
            str: The new date after subtracting the days in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the date format is incorrect.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            new_date = start - datetime.timedelta(days=days)
            return new_date.strftime('%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Incorrect date format: {e}")
