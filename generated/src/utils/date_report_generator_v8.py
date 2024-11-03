import datetime

class DateReportGenerator:
    """
    A class to generate date reports based on provided date ranges.
    """

    def __init__(self, start_date, end_date):
        """Initialize the generator with start and end dates."""
        self.start_date = start_date
        self.end_date = end_date

    def generate_report(self):
        """Generate a report of dates between start and end dates."""
        current_date = self.start_date
        report = []

        while current_date <= self.end_date:
            report.append(current_date.strftime("%Y-%m-%d"))
            current_date += datetime.timedelta(days=1)

        return report

# Example usage:
# generator = DateReportGenerator(datetime.date(2023, 1, 1), datetime.date(2023, 1, 7))
# print(generator.generate_report())
