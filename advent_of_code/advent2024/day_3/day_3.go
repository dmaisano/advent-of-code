package advent2024

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/dmaisano/advent-of-code/advent_of_code/utils"
)

func Part1(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	total := 0
	for _, line := range lines {
		result, err := processLine(line)
		if err != nil {
			return 0, fmt.Errorf("error processing line: %v", err)
		}
		total += result
	}
	return total, nil
}

func processLine(line string) (int, error) {
	// Regular expression to match valid mul(X,Y) instructions
	// where X and Y are 1-3 digit numbers
	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	matches := re.FindAllStringSubmatch(line, -1)

	sum := 0
	for _, match := range matches {
		x, err := strconv.Atoi(match[1])
		if err != nil {
			return 0, fmt.Errorf("invalid number: %s", match[1])
		}

		y, err := strconv.Atoi(match[2])
		if err != nil {
			return 0, fmt.Errorf("invalid number: %s", match[2])
		}

		sum += x * y
	}

	return sum, nil
}

func Part2(filePath string) (int, error) {
	// Read the input file
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	// Combine all lines into one string
	memory := ""
	for _, line := range lines {
		memory += line
	}

	// Regular expression to match do(), don't(), and mul(X,Y)
	re := regexp.MustCompile(`do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)`)

	// Variables to track state and sum
	sumMul := 0
	doSum := true

	// Iterate over matches
	for _, match := range re.FindAllStringSubmatch(memory, -1) {
		switch match[0] {
		case "do()":
			doSum = true
		case "don't()":
			doSum = false
		default:
			if doSum {
				// Extract numbers from the match and calculate the product
				x, _ := strconv.Atoi(match[1])
				y, _ := strconv.Atoi(match[2])
				sumMul += x * y
			}
		}
	}

	return sumMul, nil
}
