import unittest
import subprocess
import os

class TestCommitDateModifier(unittest.TestCase):
    """
    Integration tests for the commit date modification feature.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the environment for testing.
        Create a test repository and make initial commits.
        """
        cls.repo_dir = "test_repo"
        os.makedirs(cls.repo_dir, exist_ok=True)
        subprocess.run(['git', 'init'], cwd=cls.repo_dir)
        with open(os.path.join(cls.repo_dir, 'test_file.txt'), 'w') as f:
            f.write('Initial commit content')
        subprocess.run(['git', 'add', 'test_file.txt'], cwd=cls.repo_dir)
        subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=cls.repo_dir)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after tests are done.
        Remove the test repository.
        """
        for root, dirs, files in os.walk(cls.repo_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(cls.repo_dir)

    def test_commit_date_modification(self):
        """
        Test the modification of commit dates.
        """
        # Modify the commit date using the change_dates.py script
        result = subprocess.run(['python3', 'change_dates.py', '--date', '2023-01-01'], cwd=self.repo_dir, capture_output=True, text=True)

        # Check if the command executed successfully
        self.assertEqual(result.returncode, 0, f'Error: {result.stderr}')

        # Verify commit date modification
        log_output = subprocess.run(['git', 'log', '--pretty=format:%cd', '--date=iso'], cwd=self.repo_dir, capture_output=True, text=True)
        self.assertIn('2023-01-01', log_output.stdout, "Commit date was not modified correctly.")

if __name__ == '__main__':
    unittest.main()