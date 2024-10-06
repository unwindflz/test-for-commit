# date_report_generator_v4.py
# This module generates a date report based on specified criteria.
# It provides functions to format and output the report.

from datetime import datetime, timedelta

class DateReportGenerator:
    def __init__(self, start_date: str, end_date: str):
        """Initialize the report generator with a date range."""
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def generate_report(self):
        """Generate a report of dates between start and end dates."""
        date_range = self._get_date_range()
        report = self._format_report(date_range)
        return report

    def _get_date_range(self):
        """Generate a list of dates from start to end date."""
        delta = self.end_date - self.start_date
        return [self.start_date + timedelta(days=i) for i in range(delta.days + 1)]

    def _format_report(self, date_range):
        """Format the date range into a readable report."""
        report = "Date Report:\n"
        for date in date_range:
            report += f" - {date.strftime('%Y-%m-%d')}\n"
        return report

# Example usage:
# report_generator = DateReportGenerator('2023-01-01', '2023-01-10')
# print(report_generator.generate_report())