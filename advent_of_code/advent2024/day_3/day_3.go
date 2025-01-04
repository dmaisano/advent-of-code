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
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	total := 0
	for _, line := range lines {
		result, err := processLineWithConditionals(line)
		if err != nil {
			return 0, fmt.Errorf("error processing line: %v", err)
		}
		total += result
	}
	return total, nil
}

func processLineWithConditionals(line string) (int, error) {
	sum := 0
	enabled := true // Start with multiplications enabled
	pos := 0

	for pos < len(line) {
		// Look for do()
		if pos+4 <= len(line) && line[pos:pos+4] == "do()" {
			enabled = true
			pos += 4
			continue
		}

		// Look for don't()
		if pos+6 <= len(line) && line[pos:pos+6] == "don't()" {
			enabled = false
			pos += 6
			continue
		}

		// Look for mul(X,Y) pattern
		if pos+4 <= len(line) && line[pos:pos+4] == "mul(" {
			start := pos
			end := pos + 4
			parenCount := 1

			// Find the matching closing parenthesis
			for end < len(line) && parenCount > 0 {
				if line[end] == '(' {
					parenCount++
				} else if line[end] == ')' {
					parenCount--
				}
				end++
			}

			if parenCount == 0 {
				// Extract and validate the multiplication instruction
				mulInstr := line[start:end]
				re := regexp.MustCompile(`^mul\((\d{1,3}),(\d{1,3})\)$`)
				if match := re.FindStringSubmatch(mulInstr); match != nil {
					if enabled {
						x, _ := strconv.Atoi(match[1])
						y, _ := strconv.Atoi(match[2])
						sum += x * y
					}
				}
				pos = end
				continue
			}
		}

		pos++
	}

	return sum, nil
}
