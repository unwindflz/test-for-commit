import unittest

class TestUsageInstructions(unittest.TestCase):
    """
    Unit tests for the usage instructions functionality.
    """

    def test_usage_example(self):
        """
        Test case for verifying the usage example.
        """
        # Assume we have a function `get_usage_example` that returns usage instructions.
        from src.utils.data_processor import get_usage_example
        expected = "Usage: python main.py --option value"
        self.assertEqual(get_usage_example(), expected)

    def test_invalid_usage(self):
        """
        Test case for handling invalid usage inputs.
        """
        from src.utils.data_processor import validate_usage
        with self.assertRaises(ValueError):
            validate_usage("invalid_option")

    def test_usage_format(self):
        """
        Test case to ensure usage format is correct.
        """
        from src.utils.data_processor import get_usage_format
        expected_format = "--option <value>"
        self.assertIn(expected_format, get_usage_format())

if __name__ == '__main__':
    unittest.main()