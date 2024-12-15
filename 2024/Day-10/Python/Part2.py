from Util import read_input
from Part1 import index_is_out_of_bounds

def calculate_trailhead_rating(input_data, start):
    i, j = start
    sum_ = 0
    if index_is_out_of_bounds(input_data, i, j):
        return 0
    try:
        current_value = int(input_data[i][j])
        target_value = current_value + 1
    except:
        return 0
    if current_value == 9:
            return 1
    else:
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not index_is_out_of_bounds(input_data, i + direction[0], j + direction[1]):
                if input_data[i + direction[0]][j + direction[1]] == target_value:
                    sum_ += calculate_trailhead_rating(input_data, (i + direction[0], j + direction[1]))
        return sum_

def evaluate_input_part_2(input_data, zero_coords):
    trailhead_scores = []
    for zero in zero_coords:
        trailhead_scores.append(calculate_trailhead_rating(input_data, zero))
    return sum(trailhead_scores)


def main():
    # Read the input file
    input_data, zero_coords = read_input()
    print((evaluate_input_part_2(input_data, zero_coords)))

if __name__ == "__main__":
    main()
