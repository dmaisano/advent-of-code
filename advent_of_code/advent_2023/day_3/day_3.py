import re
from typing import Dict
import math

from ...utils import read_file_lines

re_symbol = r"[^\d\.]"
re_digit = r"\d+"
re_gear = r"\*"


def find_adjacent_indices(lines: list[str]) -> set[tuple[int, int]]:
    symbol_adjacent: set[tuple[int, int]] = set()
    for row, line in enumerate(lines):
        for sym in re.finditer(re_symbol, line):
            col = sym.start()
            symbol_adjacent |= set(
                (r, c) for r in range(row - 1, row + 2) for c in range(col - 1, col + 2)
            )
    return symbol_adjacent


def find_part_numbers(
    lines: list[str], symbol_adjacent: set[tuple[int, int]]
) -> set[int]:
    part_numbers = set()
    for row, line in enumerate(lines):
        for num in re.finditer(re_digit, line):
            if any((row, col) in symbol_adjacent for col in range(*num.span())):
                part_numbers.add(int(num.group()))
    return part_numbers


def find_gear_indices(lines: list[str]) -> dict[tuple[int, int], set[int]]:
    gears: Dict[tuple[int, int], set[int]] = {}
    for row, line in enumerate(lines):
        for sym in re.finditer(re_symbol, line):
            col = sym.start()
            gears[(row, col)] = []
    return gears


def fill_gears(
    lines: list[str], gears: dict[tuple[int, int], set[int]]
) -> dict[tuple[int, int], set[int]]:
    for row, line in enumerate(lines):
        for num in re.finditer(re_digit, line):
            for r in range(row - 1, row + 2):
                for c in range(num.start() - 1, num.end() + 1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(num.group()))
    return gears


def calc_gear_ratios(gears: dict[tuple[int, int], set[int]]) -> int:
    total = 0
    for _, nums in gears.items():
        if len(nums) == 2:
            total += math.prod(nums)
    return total


if __name__ == "__main__":
    lines = read_file_lines("day_3.txt")
    symbol_adjacent = find_adjacent_indices(lines)
    part_numbers = find_part_numbers(lines, symbol_adjacent)
    print(
        f"(Part 1) The sum of all part numbers in the engine schematic is: {sum(part_numbers)}"
    )
    gears = find_gear_indices(lines)
    gears = fill_gears(lines, gears)
    sum_gear_ratios = calc_gear_ratios(gears)
    print(f"(Part 2) The sum of all gear ratios is: {sum_gear_ratios}")
