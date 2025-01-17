package advent2024

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/dmaisano/advent-of-code/advent_of_code/utils"
)

func Part1(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	safeCount := 0
	for _, line := range lines {
		levels, err := parseLevels(line)
		if err != nil {
			return 0, fmt.Errorf("error parsing line '%s': %v", line, err)
		}
		if IsSafeReport(levels) {
			safeCount++
		}
	}
	return safeCount, nil
}

func parseLevels(line string) ([]int, error) {
	parts := strings.Fields(line)
	levels := make([]int, len(parts))

	for i, part := range parts {
		level, err := strconv.Atoi(part)
		if err != nil {
			return nil, fmt.Errorf("invalid number '%s': %v", part, err)
		}
		levels[i] = level
	}
	return levels, nil
}

func IsSafeReport(levels []int) bool {
	if len(levels) < 2 {
		return true
	}

	isIncreasing := true
	isDecreasing := true

	for i := 1; i < len(levels); i++ {
		diff := levels[i] - levels[i-1]

		// Check if the difference is valid
		if diff < -3 || diff > 3 || diff == 0 {
			return false
		}

		// Determine if it's not purely increasing or decreasing
		if diff > 0 {
			isDecreasing = false
		} else if diff < 0 {
			isIncreasing = false
		}
	}

	// A report is safe if it is either increasing or decreasing
	return isIncreasing || isDecreasing
}

func Part2(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	safeCount := 0
	for _, line := range lines {
		levels, err := parseLevels(line)
		if err != nil {
			return 0, fmt.Errorf("error parsing line '%s': %v", line, err)
		}
		if isSafeWithDampener(levels) {
			safeCount++
		}
	}
	return safeCount, nil
}

func isSafeWithDampener(levels []int) bool {
	// If it's already safe, no need to try removing levels
	if IsSafeReport(levels) {
		return true
	}

	// Try removing each level one at a time
	for i := 0; i < len(levels); i++ {
		// Create a new slice without the current level
		dampened := make([]int, 0, len(levels)-1)
		dampened = append(dampened, levels[:i]...)
		dampened = append(dampened, levels[i+1:]...)

		// Check if removing this level makes the sequence safe
		if IsSafeReport(dampened) {
			return true
		}
	}

	return false
}
