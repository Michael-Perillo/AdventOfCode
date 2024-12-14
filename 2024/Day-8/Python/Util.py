import os

input_file = "2024/Day-8/input.txt"

def read_input(file_path=input_file):
    # Read the input file as a list of strings
    i, j = 0, 0
    out = {}
    with open(file_path, "r") as file:
        for line in file:
            j = 0
            for char in line.strip().strip('\n'):
                if char != '.':
                    if out.get(char) is not None:
                        out[char].append((i, j))
                    else:
                        out[char] = [(i, j)]
                j += 1
            i += 1
        return out, (i, j)
