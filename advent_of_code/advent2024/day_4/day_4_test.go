package advent2024_test

import (
	"testing"

	advent2024 "github.com/dmaisano/advent-of-code/advent_of_code/advent2024/day_4"
)

func TestPart1(t *testing.T) {
	xmasCount, err := advent2024.Part1("./day_4_input.txt")
	if err != nil {
		t.Fatalf("Error calculating xmas count: %v", err)
	}
	t.Logf("Total xmas count: %d", xmasCount)
}

func TestPart2(t *testing.T) {
	xmasCount, err := advent2024.Part2("./day_4_input.txt")
	if err != nil {
		t.Fatalf("Error calculating xmas count: %v", err)
	}
	t.Logf("Total xmas count: %d", xmasCount)
}
