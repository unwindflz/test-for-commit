import datetime

class DateReportGenerator:
    """
    A class to generate date reports.
    """

    def __init__(self, start_date, end_date):
        """
        Initializes the report generator with a start and end date.
        :param start_date: The start date for the report.
        :param end_date: The end date for the report.
        """
        self.start_date = start_date
        self.end_date = end_date

    def generate_report(self):
        """
        Generates a report of dates between start_date and end_date.
        :return: A list of dates in the specified range.
        """
        report_dates = []
        current_date = self.start_date
        while current_date <= self.end_date:
            report_dates.append(current_date)
            current_date += datetime.timedelta(days=1)
        return report_dates

    def display_report(self):
        """
        Displays the generated report.
        """
        report = self.generate_report()
        for date in report:
            print(date.strftime('%Y-%m-%d'))
