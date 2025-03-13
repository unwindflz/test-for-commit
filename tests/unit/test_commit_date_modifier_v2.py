import unittest
from change_dates import modify_commit_dates  # Assuming this is the function to test

class TestCommitDateModifier(unittest.TestCase):
    def test_modify_commit_date_valid(self):
        # Test with valid parameters
        result = modify_commit_dates("2023-01-01", "2023-01-02")
        self.assertIsNotNone(result)
        self.assertEqual(result[0]['date'], "2023-01-02")  # Expected modified date

    def test_modify_commit_date_invalid(self):
        # Test with invalid parameters
        with self.assertRaises(ValueError):
            modify_commit_dates("invalid-date", "2023-01-02")  # Expecting a ValueError

    def test_modify_commit_date_no_changes(self):
        # Test when no changes should occur
        result = modify_commit_dates("2023-01-01", "2023-01-01")
        self.assertEqual(result[0]['date'], "2023-01-01")  # No modification should occur

if __name__ == '__main__':
    unittest.main()