package utils

import (
	"os"
	"path/filepath"
	"strings"
)

func readFileContents(filePath string) ([]string, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(string(data), "\n")
	return lines, nil
}

func ReadInputFile(filePath string) ([]string, error) {
	dir, err := os.Getwd()
	if err != nil {
		return nil, err
	}
	fullPath := filepath.Join(dir, filePath)
	return readFileContents(fullPath)
}
