import unittest
from typing import Type
from unittest.mock import MagicMock, patch

from advent_of_code.advent_2023.day_2.day_2 import (Counts, Game,
                                                    is_game_possible,
                                                    parse_game, part_1_soln)


class TestGameFunctions(unittest.TestCase):
    def test_parse_game(self):
        game_str = "Game 1: 2 red, 3 green, 4 blue; 1 red, 2 green, 3 blue"
        expected = Game(
            id=1,
            counts=[
                Counts(red=2, green=3, blue=4),
                Counts(red=1, green=2, blue=3)
            ]
        )
        result = parse_game(game_str)
        self.assertEqual(result, expected)

    def test_is_game_possible_true(self):
        game = Game(
            id=1,
            counts=[
                Counts(red=1, green=1, blue=1),
                Counts(red=2, green=2, blue=2)
            ]
        )
        max_counts = Counts(red=3, green=3, blue=3)
        self.assertTrue(is_game_possible(game, max_counts))

    def test_is_game_possible_false(self):
        game = Game(
            id=1,
            counts=[
                Counts(red=4, green=1, blue=1),
                Counts(red=2, green=2, blue=2)
            ]
        )
        max_counts = Counts(red=3, green=3, blue=3)
        self.assertFalse(is_game_possible(game, max_counts))

    @patch("advent_of_code.advent_2023.day_2.day_2.read_file_lines", return_value=[
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ])
    def test_part_1_soln(self, mock_games: Type[MagicMock]):
        print(mock_games)
        result = part_1_soln(mock_games.return_value)
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()
