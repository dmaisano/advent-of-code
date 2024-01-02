import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils

def calculate_points_part_1(cards):
    total_points = 0
    for card in cards:
        _, numbers = card.split(':')
        winning_numbers, your_numbers = numbers.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))
        matches = winning_numbers & your_numbers
        if matches:
            total_points += 2 ** (len(matches) - 1)
    return total_points

if __name__ == "__main__":
    debug = False
    stub_cards: list[str]  = debug and [
        "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
    ]
    cards = utils.read_file_lines("input.txt", stub_cards)
    # print(cards[-1])
    points = calculate_points_part_1(cards)
    print(f"Total points: {points}")
