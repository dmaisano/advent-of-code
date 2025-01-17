package advent2024

import (
	"strconv"
	"strings"

	"github.com/dmaisano/advent-of-code/advent_of_code/utils"
)

func Part1(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	rules := make(map[int][]int)
	var updates [][]int

	// Parse the input into rules and updates
	for _, line := range lines {
		if strings.Contains(line, "|") {
			parts := strings.Split(line, "|")
			x, _ := strconv.Atoi(parts[0])
			y, _ := strconv.Atoi(parts[1])
			rules[x] = append(rules[x], y)
		} else if line != "" {
			update := parseUpdate(line)
			updates = append(updates, update)
		}
	}

	correctUpdates := []int{}
	for _, update := range updates {
		if isOrdered(update, rules) {
			middlePage := getMiddlePage(update)
			correctUpdates = append(correctUpdates, middlePage)
		}
	}

	// Sum the middle page numbers of correctly ordered updates
	total := 0
	for _, page := range correctUpdates {
		total += page
	}

	return total, nil
}

func parseUpdate(line string) []int {
	parts := strings.Split(line, ",")
	update := make([]int, len(parts))
	for i, part := range parts {
		update[i], _ = strconv.Atoi(part)
	}
	return update
}

func isOrdered(update []int, rules map[int][]int) bool {
	// Create a map to track the position of each page
	position := make(map[int]int)
	for i, page := range update {
		position[page] = i
	}

	// Check the rules
	for x, ys := range rules {
		if _, exists := position[x]; exists {
			for _, y := range ys {
				if posY, exists := position[y]; exists {
					if position[x] > posY {
						return false // x must come before y
					}
				}
			}
		}
	}
	return true
}

func getMiddlePage(update []int) int {
	middleIndex := len(update) / 2
	return update[middleIndex]
}
