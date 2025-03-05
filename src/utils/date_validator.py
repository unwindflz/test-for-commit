import re
from datetime import datetime

# Define a set of date formats to validate against
DATE_FORMATS = [
    '%Y-%m-%d',  # ISO format
    '%d/%m/%Y',  # European format
    '%m-%d-%Y',  # US format
    '%d-%m-%Y'   # Alternative European format
]


def validate_date(date_str):
    """
    Validate if the provided date string matches any of the accepted date formats.

    Parameters:
    date_str (str): The date string to validate.

    Returns:
    bool: True if the date is valid, False otherwise.
    """
    for fmt in DATE_FORMATS:
        try:
            datetime.strptime(date_str, fmt)
            return True
        except ValueError:
            continue
    return False


def main():
    # Example usage of the date validation function
    test_dates = ['2023-10-04', '04/10/2023', '10-04-2023', '04-10-2023']
    for date in test_dates:
        result = validate_date(date)
        print(f'Date: {date}, Valid: {result}')  


if __name__ == '__main__':
    main()