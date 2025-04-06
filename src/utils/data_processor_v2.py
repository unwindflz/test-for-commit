import json
from typing import Any, Dict, List, Union

# DataProcessor class: extended functionalities for processing JSON data files.
class DataProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> Union[Dict[str, Any], None]:
        """Loads data from the specified JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            return None

    def save_data(self, data: Dict[str, Any]) -> None:
        """Saves the given data back to the JSON file."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def filter_data(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Filters the loaded data based on the provided criteria."""
        if self.data is None:
            return []
        filtered_data = []
        for item in self.data:
            if all(item.get(k) == v for k, v in criteria.items()):
                filtered_data.append(item)
        return filtered_data

    def update_data(self, updates: Dict[str, Any]) -> None:
        """Updates the loaded data with the provided updates."""
        if self.data is None:
            return
        for item in self.data:
            for key, value in updates.items():
                if key in item:
                    item[key] = value
        self.save_data(self.data)

    def get_data_summary(self) -> Dict[str, int]:
        """Provides a summary of the data, counting occurrences of each unique value.
        Returns a dictionary with unique values and their counts."""
        if self.data is None:
            return {}
        summary = {}
        for item in self.data:
            for key, value in item.items():
                summary[value] = summary.get(value, 0) + 1
        return summary

# Example usage
if __name__ == '__main__':
    processor = DataProcessor('data.json')  # Example file path
    print(processor.get_data_summary())