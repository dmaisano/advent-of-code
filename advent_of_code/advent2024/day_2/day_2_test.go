package advent2024_test

import (
	"testing"

	advent2024 "github.com/dmaisano/advent-of-code/advent_of_code/advent2024/day_2"
)

func TestPart1(t *testing.T) {
	safeCount, err := advent2024.Part1("./day_2_input.txt")
	if err != nil {
		t.Fatalf("Error calculating safe count: %v", err)
	}
	t.Logf("Safe count: %d", safeCount)
}
