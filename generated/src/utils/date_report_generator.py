import json
import datetime

class DateReportGenerator:
    """
    A class for generating date reports based on various criteria.
    """

    def __init__(self, date_list):
        """
        Initializes the DateReportGenerator with a list of dates.
        :param date_list: List of dates (as strings) in 'YYYY-MM-DD' format.
        """
        self.date_list = [datetime.datetime.strptime(date, '%Y-%m-%d') for date in date_list]

    def generate_report(self):
        """
        Generates a report summarizing the dates.
        :return: A dictionary containing the report data.
        """
        report = {
            'total_dates': len(self.date_list),
            'earliest_date': self.get_earliest_date(),
            'latest_date': self.get_latest_date(),
            'average_date': self.get_average_date()
        }
        return report

    def get_earliest_date(self):
        """
        Finds the earliest date in the date list.
        :return: The earliest date as a string in 'YYYY-MM-DD' format.
        """
        return min(self.date_list).strftime('%Y-%m-%d')

    def get_latest_date(self):
        """
        Finds the latest date in the date list.
        :return: The latest date as a string in 'YYYY-MM-DD' format.
        """
        return max(self.date_list).strftime('%Y-%m-%d')

    def get_average_date(self):
        """
        Calculates the average of the dates.
        :return: The average date as a string in 'YYYY-MM-DD' format.
        """
        avg_timestamp = sum(date.timestamp() for date in self.date_list) / len(self.date_list)
        return datetime.datetime.fromtimestamp(avg_timestamp).strftime('%Y-%m-%d')

# Example usage:
if __name__ == '__main__':
    dates = ['2023-01-01', '2023-02-01', '2023-03-01']
    report_generator = DateReportGenerator(dates)
    report = report_generator.generate_report()
    print(json.dumps(report, indent=2))
