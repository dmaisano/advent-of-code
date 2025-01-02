package advent2024_test

import (
	"testing"

	advent2024 "github.com/dmaisano/advent-of-code/advent_of_code/advent2024/day_3"
)

func TestPart1(t *testing.T) {
	total, err := advent2024.Part1("./day_3_input.txt")
	if err != nil {
		t.Fatalf("Error calculating total: %v", err)
	}
	t.Logf("Total: %d", total)
}
