import datetime

class DateReportGenerator:
    """
    A class for generating date reports based on various criteria.
    """

    def __init__(self, start_date: str, end_date: str):
        """
        Initializes the DateReportGenerator with a start and end date.
        Args:
            start_date (str): The starting date in YYYY-MM-DD format.
            end_date (str): The ending date in YYYY-MM-DD format.
        """
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    def generate_report(self):
        """
        Generates a report of dates from start_date to end_date.
        Returns:
            List[str]: A list of dates in the specified range.
        """
        report_dates = []
        current_date = self.start_date
        while current_date <= self.end_date:
            report_dates.append(current_date.strftime('%Y-%m-%d'))
            current_date += datetime.timedelta(days=1)
        return report_dates

    def get_report_summary(self):
        """
        Provides a summary of the report including total count of dates.
        Returns:
            str: A summary string.
        """
        total_dates = (self.end_date - self.start_date).days + 1
        return f'Total Dates in Report: {total_dates}'
