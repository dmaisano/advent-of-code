import unittest

from advent_of_code.advent_2023.day_3.day_3 import Part1Soln, Part2Soln


class TestDay1(unittest.TestCase):
    def setUp(self) -> None:
        self.lines = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        self.symbol_adjacent = {
            (3, 4),
            (4, 3),
            (3, 7),
            (5, 4),
            (4, 6),
            (9, 2),
            (9, 5),
            (0, 2),
            (8, 3),
            (8, 6),
            (2, 2),
            (2, 5),
            (1, 3),
            (7, 4),
            (6, 5),
            (4, 2),
            (4, 5),
            (3, 3),
            (5, 6),
            (3, 6),
            (5, 3),
            (8, 2),
            (8, 5),
            (9, 4),
            (2, 4),
            (1, 2),
            (0, 4),
            (2, 7),
            (6, 4),
            (7, 3),
            (7, 6),
            (3, 2),
            (4, 7),
            (3, 5),
            (5, 2),
            (4, 4),
            (5, 5),
            (8, 4),
            (9, 3),
            (9, 6),
            (0, 3),
            (1, 4),
            (2, 3),
            (2, 6),
            (7, 2),
            (6, 6),
            (7, 5),
        }
        self.gears = {
            (1, 3): [],
            (3, 6): [],
            (4, 3): [],
            (5, 5): [],
            (8, 3): [],
            (8, 5): [],
        }
        self.filled_gears = {
            (1, 3): [467, 35],
            (3, 6): [633],
            (4, 3): [617],
            (5, 5): [592],
            (8, 3): [664],
            (8, 5): [755, 598],
        }

    def test_find_adjacent_indices(self):
        self.assertEqual(
            self.symbol_adjacent, Part1Soln.find_adjacent_indices(self.lines)
        )

    def test_find_part_numbers(self):
        expected_part_nums = {467, 35, 633, 617, 592, 755, 664, 598}
        actual_part_nums = Part1Soln.find_part_numbers(self.lines, self.symbol_adjacent)
        self.assertEqual(expected_part_nums, actual_part_nums)
        self.assertEqual(sum(actual_part_nums), 4361)

    def test_find_gear_indices(self):
        self.assertEqual(self.gears, Part2Soln.find_gear_indices(self.lines))

    def test_fill_gears(self):
        actual_gear_ratios = Part2Soln.fill_gears(self.lines, self.gears)
        self.assertEqual(self.filled_gears, actual_gear_ratios)

    def test_calc_gear_ratios(self):
        result = Part2Soln.calc_gear_ratios(self.filled_gears)
        self.assertEqual(result, 467835)


if __name__ == "__main__":
    unittest.main()
