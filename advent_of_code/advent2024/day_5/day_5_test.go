package advent2024_test

import (
	"testing"

	advent2024 "github.com/dmaisano/advent-of-code/advent_of_code/advent2024/day_5"
)

func TestPart1(t *testing.T) {
	sum, err := advent2024.Part1("./day_5_input.txt")
	if err != nil {
		t.Fatalf("Error calculating sum: %v", err)
	}
	t.Logf("Total sum: %d", sum)
}

func TestPart2(t *testing.T) {
	sum, err := advent2024.Part2("./day_5_input.txt")
	if err != nil {
		t.Fatalf("Error calculating sum: %v", err)
	}
	t.Logf("Total sum: %d", sum)
}
