import unittest
from change_dates import modify_commit_date  # Assuming this is the function to be tested

class TestCommitDateModifier(unittest.TestCase):
    def test_modify_commit_date_valid(self):
        # Test with valid input
        result = modify_commit_date('2023-01-01', '2023-02-01')  # Example function usage
        self.assertEqual(result, '2023-02-01')  # Expecting modified commit date

    def test_modify_commit_date_invalid(self):
        # Test with invalid input
        with self.assertRaises(ValueError):
            modify_commit_date('invalid-date', '2023-02-01')  # Example error case

if __name__ == '__main__':
    unittest.main()