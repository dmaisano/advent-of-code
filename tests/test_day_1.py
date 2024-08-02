import unittest
from advent_of_code.advent_2023.day_1.day_1 import sum_calibration_values_part_1, sum_calibration_values_part_2, parse_line

class TestDay1(unittest.TestCase):
    def test_sum_calibration_values_part_1(self):
        stub = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        result = sum_calibration_values_part_1(stub)
        self.assertEqual(result, 142)

        stub = ["8carrot12", "tekashi69"]
        result = sum_calibration_values_part_1(stub)
        self.assertEqual(result, 151)

    def test_sum_calibration_values_part_2(self):
        calibration_document = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
        result = sum_calibration_values_part_2(calibration_document)
        self.assertEqual(result, 281)

        calibration_document = ["mr_robot5nine", "seven8"]
        result = sum_calibration_values_part_2(calibration_document)
        self.assertEqual(result, 137)

    def test_parse_line(self):
        line = "one7"
        result = parse_line(line)
        self.assertEqual(result, 17)

        line = "seven11"
        result = parse_line(line)
        self.assertEqual(result, 71)

if __name__ == "__main__":
    unittest.main()
