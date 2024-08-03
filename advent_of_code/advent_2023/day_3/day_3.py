import re

from ...utils import read_file_lines

re_symbol = r"[^\d\.]"
re_digit = r"\d+"


def get_adjacent_indices(lines: list[str]) -> set[tuple[int, int]]:
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


if __name__ == "__main__":
    lines = read_file_lines("day_3.txt")
    symbol_adjacent = get_adjacent_indices(lines)
    part_numbers = find_part_numbers(lines, symbol_adjacent)
    print(
        f"(Part 1) The sum of all part numbers in the engine schematic is: {sum(part_numbers)}"
    )
