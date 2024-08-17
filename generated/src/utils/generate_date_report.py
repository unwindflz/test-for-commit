#!/usr/bin/env python3

import datetime
import json
from typing import List, Dict

class DateReportGenerator:
    """
    A class to generate date reports based on a list of dates.
    """

    def __init__(self, dates: List[str]) -> None:
        """
        Initializes the DateReportGenerator with a list of date strings.
        :param dates: List of date strings (YYYY-MM-DD format)
        """
        self.dates = self._validate_dates(dates)

    def _validate_dates(self, dates: List[str]) -> List[datetime.date]:
        """
        Validates and converts date strings into date objects.
        :param dates: List of date strings
        :return: List of datetime.date objects
        """
        valid_dates = []
        for date_str in dates:
            try:
                valid_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                valid_dates.append(valid_date)
            except ValueError:
                print(f"Warning: '{date_str}' is not a valid date and will be skipped.")
        return valid_dates

    def generate_report(self) -> Dict[str, int]:
        """
        Generates a report counting the occurrences of each date.
        :return: Dictionary with dates as keys and their counts as values
        """
        report = {}
        for date in self.dates:
            report[date.isoformat()] = report.get(date.isoformat(), 0) + 1
        return report

    def save_report(self, file_path: str) -> None:
        """
        Saves the generated report to a JSON file.
        :param file_path: Path to the output JSON file
        """
        report = self.generate_report()
        with open(file_path, 'w') as json_file:
            json.dump(report, json_file, indent=4)
        print(f'Report saved to {file_path}')

# Example usage
if __name__ == '__main__':
    dates = ['2023-01-01', '2023-01-01', '2023-02-01', 'invalid-date']  # Example date list
    report_generator = DateReportGenerator(dates)
    report_generator.save_report('date_report.json')  # Save report to JSON file
