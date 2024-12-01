# Problem statement summary: Given two lists of equal length containing integers, find the "similarity score" between the two
# Similarity Score: the sum of the products of the integers in list 1 multiplied by the number of occurrences in list 2.
from Util import read_input

def find_score(list1, list2):
    # Define the score
    score = 0
    # Generate a dictionary of the occurrences of each integer in list2
    occurrences = count_occurrences(list2)
    # Iterate through list1
    for num in list1:
        # Multiply the integer by the number of occurrences in list2 if it exists
        # Otherwise, multiply the integer by 0
        occurrences_of_num = occurrences.get(num, 0)
        score += num * occurrences_of_num
    # Return the score
    return score

def count_occurrences(list):
    # Define the dictionary
    occurrences = {}
    # Iterate through the list
    for num in list:
        # If the number is already in the dictionary, increment the value
        if num in occurrences:
            occurrences[num] += 1
        # Otherwise, add the number to the dictionary
        else:
            occurrences[num] = 1
    # Return the dictionary
    return occurrences

def main():
    # read the input
    list1, list2 = read_input()
    # find the similarity score
    score = find_score(list1, list2)
    # print the score
    print(score)


main()
