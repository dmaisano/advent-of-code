import unittest

from advent_of_code.advent_2023.day_4.day_4 import Part1Soln, Part2Soln


class TestDay4Part1(unittest.TestCase):
    mock_cards1 = [
        "Card 1: 1 2 3 4 | 1 2 3 4",
        "Card 2: 1 2 3 4 | 1 2 3 4",
        "Card 3: 1 2 3 4 | 1 2 3 4",
    ]
    mock_cards2 = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    def test_find_winning_numbers(self) -> None:
        expected = [{1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}]
        self.assertEqual(Part1Soln.find_winning_numbers(self.mock_cards1), expected)

        self.assertEqual(
            Part1Soln.find_winning_numbers(self.mock_cards2),
            [
                {48, 83, 17, 86},
                {32, 61},
                {1, 21},
                {84},
                set(),
                set(),
            ],
        )

    def test_calc_points(self) -> None:
        matches = Part1Soln.find_winning_numbers(self.mock_cards1)
        self.assertEqual(Part1Soln.calc_points(matches), 24)
        matches = Part1Soln.find_winning_numbers(self.mock_cards2)
        self.assertAlmostEqual(Part1Soln.calc_points(matches), 13)


class TestDay4Part2(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
