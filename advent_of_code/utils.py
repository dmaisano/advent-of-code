from typing import Union
import os
import sys

def read_file_lines(file_path_or_stub: Union[str, list[str]]) -> list[str]:
    """Reads a text file and returns a list of its non-empty lines.

    Args:
        file_path: The path to the text file.

    Returns:
        A list of non-empty lines in the file, with any trailing newline characters removed.

    Raises:
        IOError: If there is an error opening or reading the file.
    """
    try:
        if file_path_or_stub and isinstance(file_path_or_stub, list) and len(file_path_or_stub) > 0:
            return file_path_or_stub

        # Resolve relative path based on script's directory, ensuring cross-platform compatibility
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path_or_stub = os.path.join(script_dir, file_path_or_stub)

        with open(file_path_or_stub, 'r') as file:
            lines = file.readlines()
            # Remove trailing newlines and filter out empty lines
            lines = [line.rstrip('\n') for line in lines if line.rstrip('\n')]
            return lines
    except IOError as e:
        raise IOError(f"Error reading file: {e}") from e
