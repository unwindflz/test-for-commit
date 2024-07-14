import datetime

class DateConverter:
    """
    A utility class for converting date formats.
    Provides methods to convert dates from one format to another.
    """

    def __init__(self, date_str: str, current_format: str):
        """
        Initializes the DateConverter with a date string and its format.
        
        :param date_str: The date string to be converted.
        :param current_format: The format of the input date string.
        """
        self.date_str = date_str
        self.current_format = current_format

    def convert_to(self, target_format: str) -> str:
        """
        Converts the stored date string to the target format.
        
        :param target_format: The format to which the date should be converted.
        :return: The date string in the target format.
        """
        try:
            # Parse the date string to a datetime object
            date_obj = datetime.datetime.strptime(self.date_str, self.current_format)
            # Convert the datetime object to the target format
            return date_obj.strftime(target_format)
        except ValueError as e:
            return f"Error converting date: {e}"

# Example usage
if __name__ == '__main__':
    date_converter = DateConverter('2023-03-15', '%Y-%m-%d')
    print(date_converter.convert_to('%d/%m/%Y'))  # Outputs: 15/03/2023