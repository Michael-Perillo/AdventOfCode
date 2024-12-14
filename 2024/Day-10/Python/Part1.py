from Util import read_input

def index_is_out_of_bounds(input_data, i, j):
    return i < 0 or i >= len(input_data) or j < 0 or j >= len(input_data[0])

def calculate_trailhead_score(input_data, start, trailhead_end_coords={}):
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
        if trailhead_end_coords.get(start) == None:
            trailhead_end_coords[start] = True
            return 1
        else:
            return 0
    else:
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if not index_is_out_of_bounds(input_data, i + direction[0], j + direction[1]):
                if input_data[i + direction[0]][j + direction[1]] == target_value:
                    sum_ += calculate_trailhead_score(input_data, (i + direction[0], j + direction[1]), trailhead_end_coords)
        return sum_

def evaluate_input(input_data, zero_coords):
    trailhead_scores = []
    for zero in zero_coords:
        trailhead_scores.append(calculate_trailhead_score(input_data, zero, {}))
    return sum(trailhead_scores)

def main():
    # Read the input file
    input_data, zero_coords = read_input()
    print(evaluate_input(input_data, zero_coords))

if __name__ == "__main__":
    main()
