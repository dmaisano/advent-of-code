from ...utils import read_file_lines

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
    calibration_document = read_file_lines("day_1.txt")
    part1_points = sum_calibration_values_part_1(calibration_document)
    part2_points = sum_calibration_values_part_2(calibration_document)
    print(f"Part 1 total points: {part1_points}")
    print(f"Part 2 total points: {part2_points}")
