import unittest
from typing import Type
from unittest.mock import MagicMock, patch

from advent_of_code.advent_2023.day_2.day_2 import (
    Counts,
    Game,
    calc_cube_power,
    find_minimum_cubes,
    is_game_possible,
    parse_game,
    part2_soln,
    part_1_soln,
)

part2_mock = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]


class TestGameFunctions(unittest.TestCase):
    def test_parse_game(self):
        game_str = "Game 1: 2 red, 3 green, 4 blue; 1 red, 2 green, 3 blue"
        expected = Game(
            id=1,
            counts=[Counts(red=2, green=3, blue=4), Counts(red=1, green=2, blue=3)],
        )
        result = parse_game(game_str)
        self.assertEqual(result, expected)

    def test_is_game_possible_true(self):
        game = Game(
            id=1,
            counts=[Counts(red=1, green=1, blue=1), Counts(red=2, green=2, blue=2)],
        )
        max_counts = Counts(red=3, green=3, blue=3)
        self.assertTrue(is_game_possible(game, max_counts))

    def test_is_game_possible_false(self):
        game = Game(
            id=1,
            counts=[Counts(red=4, green=1, blue=1), Counts(red=2, green=2, blue=2)],
        )
        max_counts = Counts(red=3, green=3, blue=3)
        self.assertFalse(is_game_possible(game, max_counts))

    @patch(
        "advent_of_code.advent_2023.day_2.day_2.read_file_lines",
        return_value=[
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ],
    )
    def test_part_1_soln(self, mock_games: Type[MagicMock]):
        result = part_1_soln(mock_games.return_value)
        self.assertEqual(result, 8)

    def test_find_minimum_cubes(self):
        expected_counts = [
            Counts(red=4, green=2, blue=6),
            Counts(red=1, green=3, blue=4),
            Counts(red=20, green=13, blue=6),
            Counts(red=14, green=3, blue=15),
            Counts(red=6, green=3, blue=2),
        ]
        for i in range(5):
            game = parse_game(part2_mock[i])
            self.assertEqual(find_minimum_cubes(game), expected_counts[i])

    def test_calc_cube_power(self):
        expected_cubes = [
            48,
            12,
            1560,
            630,
            36,
        ]
        for i in range(5):
            game = parse_game(part2_mock[i])
            min_cubes = find_minimum_cubes(game)
            self.assertEqual(calc_cube_power(min_cubes), expected_cubes[i])

    @patch(
        "advent_of_code.advent_2023.day_2.day_2.read_file_lines",
        return_value=part2_mock,
    )
    def test_part2_soln(self, mock_games: Type[MagicMock]):
        result = part2_soln(mock_games.return_value)
        self.assertEqual(result, 2286)


if __name__ == "__main__":
    unittest.main()
