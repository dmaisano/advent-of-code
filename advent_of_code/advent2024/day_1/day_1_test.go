package advent2024_test

import (
	"testing"

	"github.com/dmaisano/advent-of-code/advent_of_code/advent2024"
)

func TestPart1(t *testing.T) {
	totalDistance, err := advent2024.Part1("./day_1_input.txt")
	if err != nil {
		t.Fatalf("Error calculating total distance: %v", err)
	}
	t.Logf("Total distance: %d", totalDistance)
}

func TestPart2(t *testing.T) {
	totalDistance, err := advent2024.Part2("./day_1_input.txt")
	if err != nil {
		t.Fatalf("Error calculating total distance: %v", err)
	}
	t.Logf("Total distance: %d", totalDistance)
}
