import sys
import subprocess


def execute_script(file_path: str) -> None:
    """Executes the Python script at the given file path."""
    try:
        subprocess.run([sys.executable, file_path])
    except subprocess.CalledProcessError as error:
        print(f"Error executing script: {error}")
    except FileNotFoundError:
        print(f"Script file not found: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        execute_script(file_path)
    else:
        print("Usage: python main.py <file_path>")
