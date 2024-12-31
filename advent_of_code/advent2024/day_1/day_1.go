package advent2024

import (
	"math"
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

	var leftList, rightList []int

	for _, line := range lines {
		ids := strings.Fields(line)
		if len(ids) != 2 {
			continue // Skip lines that don't have exactly two IDs
		}

		leftID, err := strconv.Atoi(ids[0])
		if err != nil {
			return 0, err
		}
		rightID, err := strconv.Atoi(ids[1])
		if err != nil {
			return 0, err
		}

		leftList = append(leftList, leftID)
		rightList = append(rightList, rightID)
	}

	sort.Ints(leftList)
	sort.Ints(rightList)

	totalDistance := 0
	for i := 0; i < len(leftList); i++ {
		totalDistance += int(math.Abs(float64(leftList[i] - rightList[i])))
	}

	return totalDistance, nil
}

func Part2(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	var leftList []int
	var rightList []int

	for _, line := range lines {
		ids := strings.Fields(line)
		if len(ids) != 2 {
			continue // Skip lines that don't have exactly two IDs
		}

		leftID, err := strconv.Atoi(ids[0])
		if err != nil {
			return 0, err
		}
		rightID, err := strconv.Atoi(ids[1])
		if err != nil {
			return 0, err
		}

		leftList = append(leftList, leftID)
		rightList = append(rightList, rightID)
	}

	// Create a frequency map for the right list
	rightFrequency := make(map[int]int)
	for _, id := range rightList {
		rightFrequency[id]++
	}

	// Calculate the similarity score
	similarityScore := 0
	for _, id := range leftList {
		similarityScore += id * rightFrequency[id]
	}

	return similarityScore, nil
}
