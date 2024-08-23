import datetime

class DateCalculatorUtil:
    """
    A utility class for performing calculations on dates.
    """

    @staticmethod
    def days_between_dates(start_date: str, end_date: str) -> int:
        """
        Calculate the number of days between two dates.
        Args:
            start_date (str): The start date in 'YYYY-MM-DD' format.
            end_date (str): The end date in 'YYYY-MM-DD' format.
        Returns:
            int: The number of days between the two dates.
        Raises:
            ValueError: If the dates are not in the correct format.
        """
        try:
            start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Dates must be in 'YYYY-MM-DD' format.")
        return (end - start).days

    @staticmethod
    def add_days(date: str, days: int) -> str:
        """
        Add a number of days to a given date.
        Args:
            date (str): The date in 'YYYY-MM-DD' format.
            days (int): The number of days to add.
        Returns:
            str: The new date in 'YYYY-MM-DD' format.
        Raises:
            ValueError: If the date is not in the correct format.
        """
        try:
            base_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        new_date = base_date + datetime.timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

    @staticmethod
    def subtract_days(date: str, days: int) -> str:
        """
        Subtract a number of days from a given date.
        Args:
            date (str): The date in 'YYYY-MM-DD' format.
            days (int): The number of days to subtract.
        Returns:
            str: The new date in 'YYYY-MM-DD' format.
        Raises:
            ValueError: If the date is not in the correct format.
        """
        try:
            base_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format.")
        new_date = base_date - datetime.timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

# Example usage:
if __name__ == '__main__':
    print(DateCalculatorUtil.days_between_dates('2023-01-01', '2023-01-10'))  # Output: 9
    print(DateCalculatorUtil.add_days('2023-01-01', 10))  # Output: '2023-01-11'
    print(DateCalculatorUtil.subtract_days('2023-01-10', 5))  # Output: '2023-01-05'
