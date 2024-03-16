import unittest
import pandas as pd
from app.io.input import read_from_file, read_from_file_with_pandas


class TestFileReadFunctions(unittest.TestCase):

    def test_read_from_file(self):
        """Test that reading from a text file works correctly."""
        expected_content = "Hello, world!\n"
        self.assertEqual(read_from_file('data/test.txt'), expected_content)

    def test_read_from_file_empty(self):
        """Test that reading from an empty file returns an empty string."""
        open('empty.txt', 'w').close()
        self.assertEqual(read_from_file('empty.txt'), '')

    def test_read_from_file_with_pandas(self):
        """Test that reading from a CSV file works correctly with pandas."""
        expected_df = pd.DataFrame({
            'name': ['John', 'Doe'],
            'age': [30, 25]
        })
        pd.testing.assert_frame_equal(read_from_file_with_pandas('data/test2.csv'), expected_df)

    def test_read_from_file_with_pandas_empty(self):
        """DataFrame from an empty file should be empty."""
        open('empty.csv', 'w').close()
        expected_df = pd.DataFrame()
        pd.testing.assert_frame_equal(read_from_file_with_pandas('empty.csv'), expected_df)


if __name__ == '__main__':
    unittest.main()
