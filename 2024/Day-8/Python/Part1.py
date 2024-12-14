from Util import read_input

# an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other.
# i.e. for antennas at (x1, y1) and (x2, y2), we have a line between them defined by y = mx + c
# where m = (y2 - y1) / (x2 - x1) and c = y1 - m * x1
# The antinodes occurs at the points two slope intervals away from the initial points
# i.e. for points (x_i, y_i) the antinode occurs at (x_i + 2 * (x2 - x1), y_i + 2 * (y2 - y1))
# We should read the input data as dict of lists of tuples, where each tuple is a pair of integers representing the x and y coordinates of an antenna. The key is the antenna identifier, the value is the list of tuples
# with the input, we should also return the dimensions of the input data
# For each antenna identifier, we should iterate over all associated coordinates and calculate the antinodes between the two antennas
# If the antinode lies within the bounds of the input data, we should increment the count of that antinode in the dictionary
# If the antinode lies outside the bounds of the input data, we should skip that antinode
# We should return the number of unique antinodes in the input data
# Can use a dictionary to store the antinodes, with the key being the coordinates of the antinode and the value being the number of times that antinode occurs
# Finally, we should return the length of the dictionary

def evaluate_input(input_data, dimensions):
    # Create a dictionary to store the antinodes
    antinodes = {}
    # Iterate over the input data
    for _, coordinates_list in input_data.items():
        # Iterate over the coordinates list
        for i in range(len(coordinates_list) - 1):
            # Pick the first of the two antennas
            initial_coordinates = coordinates_list[i]
            # Iterate over the remaining antennas
            for j in range(i + 1, len(coordinates_list)):
                # Pick the second of the two antennas
                final_coordinates = coordinates_list[j]
                # Check and update the antinodes
                check_and_update_antinodes(initial_coordinates, final_coordinates, antinodes, dimensions)
    # Return the number of unique antinodes
    return len(antinodes)

def check_and_update_antinodes(initial_coordinates, final_coordinates, antinodes, dimensions):
    # use the coordinates of the two antennas to calculate the antinode coordinates
    x1, y1 = initial_coordinates
    x2, y2 = final_coordinates
    # Calculate the pair of antinode coordinates for the two antennas
    antinode_x1 = x1 + 2 * (x2 - x1)
    antinode_y1 = y1 + 2 * (y2 - y1)

    antinode_x2 = x2 + 2 * (x1 - x2)
    antinode_y2 = y2 + 2 * (y1 - y2)

    # Check if the antinode lies within the bounds of the input data
    if antinode_lies_in_dimensions(antinode_x1, antinode_y1, dimensions):
        update_antinodes(antinode_x1, antinode_y1, antinodes)
    if antinode_lies_in_dimensions(antinode_x2, antinode_y2, dimensions):
        update_antinodes(antinode_x2, antinode_y2, antinodes)

def antinode_lies_in_dimensions(antinode_x, antinode_y, dimensions):
    rows, cols = dimensions
    return 0 <= antinode_x < rows and 0 <= antinode_y < cols

def update_antinodes(antinode_x, antinode_y, antinodes):
    if antinodes.get((antinode_x, antinode_y)) is not None:
        antinodes[(antinode_x, antinode_y)] += 1
    else:
        antinodes[(antinode_x, antinode_y)] = 1

def main():
    # Read the input file
    input_data, dimensions = read_input()
    print(evaluate_input(input_data, dimensions))

if __name__ == "__main__":
    main()
