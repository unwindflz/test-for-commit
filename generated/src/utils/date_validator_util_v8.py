def is_valid_date(date_string, date_format='%Y-%m-%d'):
    """Check if the provided date string is valid according to the specified format.

    Args:
        date_string (str): The date string to validate.
        date_format (str): The format to validate against. Defaults to '%Y-%m-%d'.

    Returns:
        bool: True if the date string is valid, False otherwise.
    """
    from datetime import datetime
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def format_date(date_string, input_format='%Y-%m-%d', output_format='%d-%m-%Y'):
    """Format a date string from one format to another.

    Args:
        date_string (str): The date string to format.
        input_format (str): The current format of the date string. Defaults to '%Y-%m-%d'.
        output_format (str): The format to convert the date string to. Defaults to '%d-%m-%Y'.

    Returns:
        str: The formatted date string.
    """
    from datetime import datetime
    try:
        date_obj = datetime.strptime(date_string, input_format)
        return date_obj.strftime(output_format)
    except ValueError:
        return "Invalid date"
