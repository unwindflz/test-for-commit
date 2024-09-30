# date_report_generator_v3.py
# This module is responsible for generating date reports.
# It provides functions to create a summary of date-related data.

from datetime import datetime, timedelta

class DateReportGenerator:
    def __init__(self, start_date: str, end_date: str):
        """Initialize the date report generator with a date range."
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')

    def generate_report(self):
        """Generate a date report between start and end dates."""
        report = []
        current_date = self.start_date
        while current_date <= self.end_date:
            report.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)
        return report

    def get_summary(self):
        """Get a summary of the report."""
        total_days = (self.end_date - self.start_date).days + 1
        return {
            'total_days': total_days,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d')
        }