import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import utils


def sum_calibration_values_part_1(calibration_document: list[str]) -> int:
    total_sum = 0
    for line in calibration_document:
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in line[::-1] if char.isdigit()), None)
        if first_digit and last_digit:
            total_sum += int(first_digit + last_digit)
    return total_sum


if __name__ == "__main__":
    debug = False
    stub: list[str] = debug and [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]
    calibration_document = utils.read_file_lines("input.txt", stub)
    points = sum_calibration_values_part_1(calibration_document)
    print(f"Total points: {points}")
