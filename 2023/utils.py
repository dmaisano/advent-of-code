import os
import sys


def read_file_lines(file_path: str, stub: list[str] = []) -> list[str]:
    """Reads a text file and returns a list of its non-empty lines.

    Args:
        file_path: The path to the text file.

    Returns:
        A list of non-empty lines in the file, with any trailing newline characters removed.

    Raises:
        IOError: If there is an error opening or reading the file.
    """
    if stub and len(stub) > 0:
        return stub

    try:
         # Resolve relative path based on script's directory, ensuring cross-platform compatibility
        script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path = os.path.join(script_dir, file_path)

        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Remove trailing newlines and filter out empty lines
            lines = [line.rstrip('\n') for line in lines if line.rstrip('\n')]
            return lines
    except IOError as e:
        raise IOError(f"Error reading file: {e}") from e
