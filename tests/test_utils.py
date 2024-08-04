import os
import sys
import unittest
from unittest.mock import mock_open, patch

from advent_of_code.utils import read_file_lines


class TestReadFileLines(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="line1\n\nline2\nline3\n")
    def test_read_file_lines_from_file(self, mock_file):
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path = "test.txt"
        expected_path = os.path.join(script_dir, file_path)

        result = read_file_lines(file_path)

        mock_file.assert_called_once_with(expected_path, "r")
        self.assertEqual(result, ["line1", "line2", "line3"])

    def test_read_file_lines_from_list(self):
        lines = ["line1", "line2", "line3"]
        result = read_file_lines(lines)
        self.assertEqual(result, lines)

    @patch("builtins.open", new_callable=mock_open)
    def test_read_file_lines_empty_file(self, mock_file):
        mock_file.return_value.readlines.return_value = []
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path = "test.txt"
        expected_path = os.path.join(script_dir, file_path)

        result = read_file_lines(file_path)

        mock_file.assert_called_once_with(expected_path, "r")


if __name__ == "__main__":
    unittest.main()
