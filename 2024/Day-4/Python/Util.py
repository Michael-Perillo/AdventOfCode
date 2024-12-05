import os

input_file = "2024/Day-4/input.txt"

def read_input():
    # Read the input file as a list of strings
    with open(input_file, "r") as file:
        return [line for line in file]
