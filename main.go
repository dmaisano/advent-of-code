package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/dmaisano/advent-of-code/advent_of_code/utils"
)

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

// Example usage
func main() {
	result, err := Part2("./advent_of_code/advent2024/day_3/day_3_input.txt")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println("Sum of enabled multiplications:", result)
}
