# date_report_generator_util_v3.py
# This utility generates detailed reports based on date data.

from datetime import datetime
from typing import List, Dict

class DateReportGenerator:
    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initialize with date data.
        Args:
            data (List[Dict[str, str]]): List of dictionaries containing date information.
        """
        self.data = data

    def generate_report(self) -> str:
        """Generates a report of the date data.
        Returns:
            str: Formatted report as a string.
        """
        report_lines = ["Date Report:\n"]
        for entry in self.data:
            date_str = entry.get('date')
            description = entry.get('description', 'No description')
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            report_lines.append(f"Date: {date_obj.strftime('%B %d, %Y')} - Description: {description}")
        return '\n'.join(report_lines)

# Example usage:
# data = [{'date': '2023-01-01', 'description': 'New Year'}, {'date': '2023-02-14', 'description': 'Valentine's Day'}]
# generator = DateReportGenerator(data)
# print(generator.generate_report())