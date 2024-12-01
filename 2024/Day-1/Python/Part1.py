# Problem statement summary: Given two lists of equal length containing integers, find the "distance" between the two
# Distance: the sum of the difference between the two smallest integers in the list. Once we find the smallest, we
# remove them from their lists and find the next smallest integers.
from Util import read_input

def find_distance(list1, list2):
    # Sort both lists
    list1.sort()
    list2.sort()

    # Define the distance
    distance = 0

    # Iterate through the sorted lists and calculate the distance
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])

    # Return the distance
    return distance


def main():
    # Read the input
    list1, list2 = read_input()
    # Find the distance
    distance = find_distance(list1, list2)
    # Print the distance
    print(distance)


main()
