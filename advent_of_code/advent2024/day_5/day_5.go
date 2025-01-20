package advent2024

import (
	"sort"
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

func Part2(filePath string) (int, error) {
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

	incorrectUpdates := [][]int{}
	for _, update := range updates {
		if !isOrdered(update, rules) {
			// Store a copy of the update
			updateCopy := make([]int, len(update))
			copy(updateCopy, update)
			incorrectUpdates = append(incorrectUpdates, updateCopy)
		}
	}

	// Sort each incorrect update according to rules
	total := 0
	for _, update := range incorrectUpdates {
		sortedUpdate := sortUpdate(update, rules)
		middlePage := getMiddlePage(sortedUpdate)
		total += middlePage
	}

	return total, nil
}

func sortUpdate(update []int, rules map[int][]int) []int {
	// Create a copy of the update slice
	sorted := make([]int, len(update))
	copy(sorted, update)

	// Sort using custom less function
	sort.Slice(sorted, func(i, j int) bool {
		x, y := sorted[i], sorted[j]

		// Check if there's a direct rule x -> y
		if deps, exists := rules[y]; exists {
			for _, dep := range deps {
				if dep == x {
					return false // y depends on x, so x should come first
				}
			}
		}

		// Check if there's a direct rule y -> x
		if deps, exists := rules[x]; exists {
			for _, dep := range deps {
				if dep == y {
					return true // x depends on y, so y should come first
				}
			}
		}

		// If no direct rules, maintain relative order
		return x > y
	})

	return sorted
}
