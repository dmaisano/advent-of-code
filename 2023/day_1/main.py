import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import utils

digit_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def sum_calibration_values_part_1(calibration_document: list[str]) -> int:
    total_sum = 0
    for line in calibration_document:
        first_digit = next((char for char in line if char.isdigit()), None)
        last_digit = next((char for char in line[::-1] if char.isdigit()), None)
        if first_digit and last_digit:
            total_sum += int(first_digit + last_digit)
    return total_sum


def sum_calibration_values_part_2(calibration_document: list[str]) -> int:
    total_sum = 0
    for line in calibration_document:
        total_sum += parse_line(line)
    return total_sum


def parse_line(line: str) -> int:
    digits: list[str] = []

    for i in range(0, len(line)):
        char = line[i]
        if char.isdigit():
            digits.append((char))
            continue

        sub_str = line[i:]
        for [key, value] in digit_mapping.items():
            if sub_str.startswith(key):
                digits.append(value)
                break

    return int(digits[0] + digits[-1])


if __name__ == "__main__":
    debug = False
    stub_part_2: list[str] = debug and [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    stub_part_1: list[str] = debug and [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet",
    ]

    calibration_document = utils.read_file_lines("input.txt", stub_part_2)
    points = sum_calibration_values_part_2(calibration_document)
    print(f"Total points: {points}")
