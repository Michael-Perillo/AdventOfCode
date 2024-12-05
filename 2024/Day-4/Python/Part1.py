from Util import read_input

# Part 1: Word search
# Find all occurrences of XMAS in a list of strings
# The occurrences can be in any direction (horizontal, vertical, diagonal), and can overlap
# The strings are all equal in length

# This is a brute force solution
def count_xmas_occurrences(input_data):
    words = ["XMAS", "SAMX"]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    ranges = []
    count = 0
    for word in words:
        for i in range(len(input_data)):
            row = input_data[i]
            for j in range(len(row)):
                char = row[j]
                if char == word[0] and not any((i, j) in range_ for range_ in ranges):
                    potential_range_start = (i, j)
                    for direction in directions:
                        x, y = direction
                        for k in range(1, len(word)):
                            row_index = i + k*x
                            col_index = j + k*y
                            if 0 <= row_index < len(input_data) and 0 <= col_index < len(row):
                                if input_data[i + k*x][j + k*y] != word[k]:
                                    break
                            else:
                                break
                        else:
                            ranges.append((potential_range_start, (row_index, col_index)))
                            count += 1
    return count


def main():
    # Read the input file
    input_data = read_input()
    # Count the number of XMAS occurrences
    print(count_xmas_occurrences(input_data))

if __name__ == "__main__":
    main()
