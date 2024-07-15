import json
import os
from typing import Any, Dict

class DataProcessor:
    """
    A class for processing JSON data files.
    This class provides methods to load, process, and save data.
    """

    def __init__(self, file_path: str):
        """
        Initializes the DataProcessor with a specified file path.
        :param file_path: Path to the JSON data file.
        """
        self.file_path = file_path

    def load_data(self) -> Dict[str, Any]:
        """
        Loads data from the JSON file.
        :return: Data loaded from the JSON file.
        """
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"The file {self.file_path} does not exist.")
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON from the file: {self.file_path}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading data: {e}")

    def save_data(self, data: Dict[str, Any]) -> None:
        """
        Saves data to the JSON file.
        :param data: Data to be saved to the JSON file.
        """
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise RuntimeError(f"An error occurred while saving data: {e}")

    def process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes the loaded data (placeholder for actual processing logic).
        :param data: Data to be processed.
        :return: Processed data.
        """
        # Implement your processing logic here
        return data  # Currently, it just returns the input data unchanged
