package main

// Problem statement summary: Given two lists of equal length containing integers, find the "similarity score" between the two
// Similarity Score: the sum of the products of the integers in list 1 multiplied by the number of occurrences in list 2

func CalculateSimilarityScore(array1 []int, array2 []int) int {
	// Define the similarity score
	score := 0
	// Count the occurrences of each integer in the second array and store them in a map
	occurrences := CountOccurrences(array2)
	// Iterate over the first array
	for _, value := range array1 {
		// Multiply the value by the number of occurrences in the second array and add it to the score
		score += value * occurrences[value]
	}
	return score
}

// Define a function to count the occurrences of each integer in an array and store them in a map
func CountOccurrences(array []int) map[int]int {
	// Define the map to store the occurrences
	occurrences := make(map[int]int)
	// Iterate over the array
	for _, value := range array {
		// Increment the occurrence count for the value
		occurrences[value]++
	}
	// Return the map
	return occurrences
}
