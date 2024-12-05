from Util import read_input
import re

# Part 2: Instead of counting the number of occurrences of the words XMAS and SAMX, find the number of X shaped MAS occurrences
# I.e. the occurrences of the word MAS that form an X shape, as shown:
# M.S
# .A.
# M.S

def is_valid_x_shaped_mas(input_data, i, j):
    # use regex to check if the top and bottom rows are valid
    # there are 4 possible patterns for the top and bottom rows
    # M.S, S.M, M.M, S.S
    # if the top row is M.S, the bottom row must M.S as well and vice versa
    # if the top row is M.M, the bottom row must be S.S and vice versa
    # we already know that the middle row is A
    # ignore the middle character on the top and bottom rows
    valid_regex = [r"M.S", r"S.M", r"M.M", r"S.S"]
    top_row = input_data[i][j:j+3]
    bottom_row = input_data[i + 2][j:j+3]
    if re.match(valid_regex[0], top_row) and re.match(valid_regex[0], bottom_row):
        return True
    if re.match(valid_regex[1], top_row) and re.match(valid_regex[1], bottom_row):
        return True
    if re.match(valid_regex[2], top_row) and re.match(valid_regex[3], bottom_row):
        return True
    if re.match(valid_regex[3], top_row) and re.match(valid_regex[2], bottom_row):
        return True
    return False

def count_x_shaped_mas_occurrences(input_data):
    count = 0
    for i in range(len(input_data) - 2):
        for j in range(len(input_data[i]) - 2):
            # check if the window contains an X shaped MAS
            # the middle character must be A
            # the other characters must be M or S
            # if one of the corners is an M, the other must be an S and vice versa
            if input_data[i + 1][j + 1] == "A":
                if is_valid_x_shaped_mas(input_data, i, j):
                    count += 1
    return count

def main():
    # Read the input file
    input_data = read_input()
    # Count the number of X shaped MAS occurrences
    print(count_x_shaped_mas_occurrences(input_data))

if __name__ == "__main__":
    main()
