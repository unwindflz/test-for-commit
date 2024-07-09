#!/usr/bin/env python3

import datetime
import random
import yaml

class DateChange:
    """
    A class to handle operations related to changing dates.
    """

    def __init__(self, date_format='%Y-%m-%d'):
        """
        Initializes the DateChange object with a specific date format.
        :param date_format: The format to use for date representation.
        """
        self.date_format = date_format

    def random_date(self, start_date, end_date):
        """
        Generates a random date between two given dates.
        :param start_date: The start date as a string in the specified format.
        :param end_date: The end date as a string in the specified format.
        :return: A random datetime.date object.
        """
        try:
            start = datetime.datetime.strptime(start_date, self.date_format)
            end = datetime.datetime.strptime(end_date, self.date_format)
            return start + datetime.timedelta(days=random.randint(0, (end - start).days))
        except ValueError as e:
            print(f'Error: {e}')  # Handle invalid date format

    def format_date(self, date):
        """
        Formats a given date to the specified date format.
        :param date: A datetime.date object.
        :return: A string representation of the date in the specified format.
        """
        try:
            return date.strftime(self.date_format)
        except Exception as e:
            print(f'Error formatting date: {e}')  # Handle unexpected errors

    def load_dates_from_yaml(self, yaml_file):
        """
        Loads dates from a YAML file.
        :param yaml_file: Path to the YAML file containing dates.
        :return: A list of dates loaded from the YAML file.
        """
        try:
            with open(yaml_file, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            print(f'Error: The file {yaml_file} was not found.')
            return []
        except yaml.YAMLError as e:
            print(f'YAML error: {e}')  # Handle YAML parsing errors
