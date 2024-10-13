# date_report_generator_v5.py
# This module generates a report based on date data.

from datetime import datetime, timedelta

class DateReportGenerator:
    def __init__(self, start_date, end_date):
        """
        Initializes the report generator with a date range.
        
        :param start_date: The starting date for the report.
        :param end_date: The ending date for the report.
        """
        self.start_date = start_date
        self.end_date = end_date

    def generate_report(self):
        """
        Generates a date report for the given date range.
        
        :return: A string report summarizing the date range.
        """
        total_days = (self.end_date - self.start_date).days
        report = f"Date Report\nStart Date: {self.start_date.strftime('%Y-%m-%d')}\nEnd Date: {self.end_date.strftime('%Y-%m-%d')}\nTotal Days: {total_days}"
        return report

# Example usage
if __name__ == '__main__':
    start = datetime(2023, 1, 1)
    end = datetime(2023, 12, 31)
    generator = DateReportGenerator(start, end)
    print(generator.generate_report())