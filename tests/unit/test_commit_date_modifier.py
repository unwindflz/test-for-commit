import unittest
from change_dates import modify_commit_date  # Assuming this function exists in change_dates.py

class TestCommitDateModifier(unittest.TestCase):
    def test_modify_commit_date_valid(self):
        # Test with valid date modification
        result = modify_commit_date('2023-01-01', new_date='2023-01-02')
        self.assertEqual(result, 'Commit date changed to 2023-01-02')

    def test_modify_commit_date_invalid(self):
        # Test with invalid date
        with self.assertRaises(ValueError):
            modify_commit_date('invalid-date', new_date='2023-01-02')

    def test_modify_commit_date_no_change(self):
        # Test with no change in date
        result = modify_commit_date('2023-01-01', new_date='2023-01-01')
        self.assertEqual(result, 'No change in commit date')

if __name__ == '__main__':
    unittest.main()