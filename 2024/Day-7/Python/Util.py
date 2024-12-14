import os

input_file = "2024/Day-7/input.txt"

def read_input(file_path=input_file):
    # Read the input file as a list of strings
    with open(file_path, "r") as file:
        out = {}
        for line in file:
            split_line = line.split(':')
            # the left side of the colon is the result of the function
            # the right side is the input
            out[int(split_line[0])] = [int(digit) for digit in split_line[1].strip().split()]
        return out
