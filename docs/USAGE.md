# Usage Instructions for Test for Commit

This document provides usage instructions for the main features of the **Test for Commit** project, which allows users to modify commit dates in Git repositories based on specified configurations.

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com-unwindflz:unwindflz/test-for-commit.git
   cd test-for-commit
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Modifying Commit Dates

To modify commit dates, you need to provide a configuration file. The configuration file should be in YAML format and specify the desired modifications.

### Example Configuration File

```yaml
# commit_date_config.yaml

modifications:
  - commit_hash: "abc123"
    new_date: "2023-01-01T12:00:00"
  - commit_hash: "def456"
    new_date: "2023-01-02T15:30:00"
```

### Running the Date Modifier

To apply the modifications defined in your configuration file, run the following command:
```bash
python change_dates.py --config commit_date_config.yaml
```

## Validating Dates

Before processing, you can validate the dates in your configuration file by using the date validator utility. Ensure that the dates are in the correct format.

### Command to Validate Dates

To validate the dates, use:
```bash
python -m src.utils.date_validator --file commit_date_config.yaml
```

## Additional Features

- **Data Processing Utilities:** This project also includes utility functions for processing JSON data files used by the commit date modifier. You can find these utilities in the `src/utils` directory.
- **Logging and Error Handling:** The application includes logging to help track the processing steps and any potential errors.

## FAQs
For more information, please refer to the [FAQ document](FAQ.md) in the docs directory for common questions and troubleshooting tips.

## Conclusion
This documentation provides a basic overview of how to use the Test for Commit project. For more detailed information about contributing, installation, and features, please refer to the other documents in the `docs` directory.