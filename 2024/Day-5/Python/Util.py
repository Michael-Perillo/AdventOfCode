import os
import re

file_path = "2024/Day-5/Input.txt"

def read_input(input_file_path=file_path):
    # we return two things: the ordering dictionary and the messages
    # the first set of lines from the file are key value pairs
    # the second set of lines are the messages, which are lists of integers
    # the first and second set of lines are separated by a blank line
    # the key value pairs are separated by a | character
    # read the first set of lines into a dictionary, then read the second set of lines into a list of lists
    ordering = {}
    messages = []

    with open(input_file_path, "r") as file:
        for line in file:
            if re.match(r".*\|.*", line):
                values = line.strip().split("|")
                key, value = int(values[0]), int(values[1])
                if key not in ordering:
                    ordering[key] = [value]
                else:
                    ordering[key].append(value)
            else:
                if line.strip() == "":
                    continue
                messages.append([int(x) for x in line.strip().split(",")])
    return ordering, messages
