import unittest
from change_dates import modify_commit_dates

class TestCommitDateModifier(unittest.TestCase):

    def test_modify_commit_dates_valid(self):
        # Test with valid date modification
        result = modify_commit_dates('2021-01-01', '2021-01-02')
        self.assertEqual(result, 'Commit date modified to 2021-01-02')

    def test_modify_commit_dates_invalid(self):
        # Test with invalid date
        with self.assertRaises(ValueError):
            modify_commit_dates('invalid-date', '2021-01-02')

    def test_modify_commit_dates_no_change(self):
        # Test with same dates
        result = modify_commit_dates('2021-01-01', '2021-01-01')
        self.assertEqual(result, 'No modification made, dates are the same')

if __name__ == '__main__':
    unittest.main()