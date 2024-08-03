from pydantic import BaseModel

from ...utils import read_file_lines


class Counts(BaseModel):
    red: int = 0
    green: int = 0
    blue: int = 0


class Game(BaseModel):
    id: int
    counts: list[Counts] = []


cube_counts = (12, 13, 14)

def parse_game(game_str: str) -> Game:
    id_part, *count_parts = game_str.split(": ")
    count_parts = count_parts[0].split("; ")
    counts: list[Counts] = []

    for count_part in count_parts:
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        part = count_part.split(", ")

        for color_part in part:
            count, color = color_part.split(" ")
            colors[color] = int(count, 10)

        counts.append(Counts(**colors))

    id = int(id_part.replace("Game ", ""))
    return Game(id=id, counts=counts)


def is_game_possible(game: Game, max_counts: Counts) -> bool:
    return all(
        counts.red <= max_counts.red
        and counts.green <= max_counts.green
        and counts.blue <= max_counts.blue
        for counts in game.counts
    )


def part_1_soln(games: list[str]) -> int:
    red_count, green_count, blue_count = cube_counts
    possible_game_ids: list[int] = []

    for game_id, game in enumerate(games, start=1):
        parsed_game = parse_game(game)
        if is_game_possible(
            parsed_game, Counts(red=red_count, green=green_count, blue=blue_count)
        ):
            possible_game_ids.append(game_id)

    return sum(possible_game_ids)

if __name__ == "__main__":
    games = read_file_lines("day_2.txt")
    sum_game_ids = part_1_soln(games)
    print(f"Part 1 total points: {sum_game_ids}")
