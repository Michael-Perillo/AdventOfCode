package main

import (
	"io"
	"os"
	"strconv"
	"strings"
)

// Define a function to read the input file
func ReadInputFile() ([]int, []int) {
	// Define the path to the input file
	path := "../Input.txt"
	// Open the input file
	file, _ := os.Open(path)
	// Read the input file
	input, _ := io.ReadAll(file)
	// Convert the input to a string
	inputString := string(input)
	// Split the input by newlines
	inputArray := strings.Split(inputString, "\r\n")
	// Remove the last element of the array (empty string)
	inputArray = inputArray[:len(inputArray)-1]
	// Define the two arrays to store the input
	array1 := []int{}
	array2 := []int{}
	// Iterate over the input array
	for _, value := range inputArray {
		// Split the value by spaces
		valueArray := strings.Split(value, "   ")
		// Convert the first value to an integer
		int1, _ := strconv.Atoi(valueArray[0])
		// Convert the second value to an integer
		int2, _ := strconv.Atoi(valueArray[1])
		// Append the integers to the arrays
		array1 = append(array1, int1)
		array2 = append(array2, int2)
	}
	// Return the arrays
	return array1, array2
}
