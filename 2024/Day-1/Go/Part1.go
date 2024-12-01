package main

import (
	"sort"
)

// Problem statement summary: Given two lists of equal length containing integers, find the "distance" between the two
// Distance: the sum of the difference between the two smallest integers in the list.

func CalculateDistance(list1 []int, list2 []int) int {
	// Define the distance variable
	distance := 0
	// Sort the lists in ascending order
	sort.Ints(list1)
	sort.Ints(list2)
	// Iterate over the lists
	for i := 0; i < len(list1); i++ {
		// Add the absolute difference between the two integers to the distance
		newDistance := list1[i] - list2[i]
		if newDistance < 0 {
			newDistance *= -1
		}
		distance += newDistance
	}
	// Return the distance
	return distance
}
