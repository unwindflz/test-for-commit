# Data Report Generator v8
# This module generates a detailed report based on provided date data.

from datetime import datetime

class DataReportGenerator:
    def __init__(self, data):
        """Initialize the report generator with data."""
        self.data = data

    def generate_report(self):
        """Generate a detailed report."""
        report = "Data Report:\n"
        for entry in self.data:
            report += f"Date: {entry['date']}, Value: {entry['value']}\n"
        return report

    def save_report(self, filename):
        """Save the generated report to a file."""
        with open(filename, 'w') as f:
            f.write(self.generate_report())

# Example usage:
if __name__ == '__main__':
    data = [{'date': '2023-01-01', 'value': 100}, {'date': '2023-01-02', 'value': 150}]
    generator = DataReportGenerator(data)
    generator.save_report('data_report.txt')
