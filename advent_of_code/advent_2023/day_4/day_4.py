import re
from ...utils import read_file_lines


class Part1Soln:
    @staticmethod
    def find_winning_numbers(cards: list[str]) -> list[set[int]]:
        result: list[set[int]] = []
        for card in cards:
            winning_numbers_str, your_numbers_str = re.sub(
                r"^Card \d: ", "", card
            ).split(" | ")
            winning_numbers = set(map(int, winning_numbers_str.split()))
            your_numbers = list(map(int, your_numbers_str.split()))
            result.append(winning_numbers.intersection(your_numbers))
        return result

    @staticmethod
    def calc_points(matches: list[set[int]]) -> int:
        total_points = 0
        for match in matches:
            if len(matches) <= 0:
                continue
            print(match, len(match))
            total_points += 1 * (2 * len(match)) if len(matches) > 1 else 1
        return total_points


class Part2Soln:
    pass


if __name__ == "__main__":
    cards = read_file_lines("day_4.txt")
    matches = Part1Soln.find_winning_numbers(cards)
    total_points = Part1Soln.calc_points(matches)
    print(f"(Part 1) Total points: {total_points}")
