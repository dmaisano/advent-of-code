package advent2024

import (
	"fmt"

	"github.com/dmaisano/advent-of-code/advent_of_code/utils"
)

// Directions to traverse the grid: horizontal, vertical, diagonal
var directions = [][2]int{
	{0, 1},   // right
	{0, -1},  // left
	{1, 0},   // down
	{-1, 0},  // up
	{1, 1},   // diagonal down-right
	{-1, -1}, // diagonal up-left
	{-1, 1},  // diagonal up-right
	{1, -1},  // diagonal down-left
}

func Part1(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath)
	if err != nil {
		return 0, err
	}

	word := "XMAS"
	rows := len(lines)
	if rows == 0 {
		return 0, fmt.Errorf("empty grid")
	}
	cols := len(lines[0])

	count := 0

	// Helper function to check if a word can be formed starting from (x, y) in a specific direction
	canFormWord := func(x, y, dx, dy int) bool {
		for i := 0; i < len(word); i++ {
			nx, ny := x+i*dx, y+i*dy
			if nx < 0 || ny < 0 || nx >= rows || ny >= cols || lines[nx][ny] != word[i] {
				return false
			}
		}
		return true
	}

	// Traverse the grid and look for the word in all directions
	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			for _, dir := range directions {
				dx, dy := dir[0], dir[1]
				if canFormWord(x, y, dx, dy) {
					count++
				}
			}
		}
	}

	return count, nil
}
