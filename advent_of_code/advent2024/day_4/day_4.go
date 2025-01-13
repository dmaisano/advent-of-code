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

// isMAS checks if the given 3-letter string is "MAS" or "SAM".
func isMAS(s string) bool {
	return s == "MAS" || s == "SAM"
}

// Part2 solves the "X-MAS" puzzle.
func Part2(filePath string) (int, error) {
	lines, err := utils.ReadInputFile(filePath) // or use your own method to read lines
	if err != nil {
		return 0, err
	}

	// Convert lines into a 2D grid of runes (characters).
	// This way we can index [row][col] easily.
	grid := make([][]rune, len(lines))
	for i := range lines {
		grid[i] = []rune(lines[i])
	}
	rows := len(grid)
	if rows == 0 {
		return 0, fmt.Errorf("no input")
	}
	cols := len(grid[0]) // assuming rectangular input

	count := 0

	// We only scan where a 3x3 "X" can fully fit
	// That means up to rows-2 and cols-2 (0-based indexing).
	for r := 0; r < rows-2; r++ {
		for c := 0; c < cols-2; c++ {
			// Diagonal 1 (top-left to bottom-right)
			d1 := []rune{
				grid[r][c],
				grid[r+1][c+1],
				grid[r+2][c+2],
			}

			// Diagonal 2 (top-right to bottom-left)
			d2 := []rune{
				grid[r][c+2],
				grid[r+1][c+1],
				grid[r+2][c],
			}

			// Convert to string
			diag1 := string(d1)
			diag2 := string(d2)

			// If both diagonals form "MAS" or "SAM", we've found an X-MAS
			if isMAS(diag1) && isMAS(diag2) {
				count++
			}
		}
	}

	return count, nil
}
