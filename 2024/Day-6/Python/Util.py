import os
import re

file_path = "2024/Day-6/Input.txt"

def read_input(input_file_path=file_path):
    # returns the list of strings representing the map and the starting position's coordinates
    out = []
    i = 0
    j = 0
    with open(input_file_path, "r") as file:
        for line in file:
            if line.strip() == "":
                continue
            out.append(line.strip())
            if "^" in line:
                j = line.index("^")
                i = len(out) - 1
    return out, (i, j)
