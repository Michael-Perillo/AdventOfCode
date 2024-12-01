package main

// Driver code for parts 1 and 2

func main() {
	// Call the part1 function
	part1()
	// Call the part2 function
	part2()
}

func part1() {
	// Read the input file
	array1, array2 := ReadInputFile()
	// Calculate the distance between the two lists
	distance := CalculateDistance(array1, array2)
	// Print the distance
	println(distance)
}

func part2() {
	// Read the input file
	array1, array2 := ReadInputFile()
	// Calculate the similarity score between the two lists
	score := CalculateSimilarityScore(array1, array2)
	// Print the similarity score
	println(score)
}
