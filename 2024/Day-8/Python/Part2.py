from Util import read_input

# Now, antinodes can be defined at any distance between two antennae, not just at twice the distance. We should update the check_and_update_antinodes function to calculate the antinode coordinates at all distances between the two antennae

def evaluate_input_part_2(input_data, dimensions):
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
    # Calculate all anti-nodes between the two antennas
    antinode_list = calculate_antinodes(initial_coordinates, final_coordinates, dimensions)
    # Update the antinodes dictionary
    for antinode in antinode_list:
        update_antinodes(antinode[0], antinode[1], antinodes)

def calculate_antinodes(initial_coordinates, final_coordinates, dimensions):
    antinode_list = [initial_coordinates, final_coordinates]
    x1, y1 = initial_coordinates
    x2, y2 = final_coordinates
    m_x1 = x2 - x1
    m_y1 = y2 - y1
    m_x2 = x1 - x2
    m_y2 = y1 - y2
    antinode_x1 = x1 + m_x1
    antinode_y1 = y1 + m_y1
    propagate_antinodes(antinode_list, antinode_x1, antinode_y1, m_x1, m_y1, dimensions)

    antinode_x2 = x2 + m_x2
    antinode_y2 = y2 + m_y2
    propagate_antinodes(antinode_list, antinode_x2, antinode_y2, m_x2, m_y2, dimensions)
    return antinode_list

def propagate_antinodes(antinode_list, antinode_x, antinode_y, m_x, m_y, dimensions):
    while antinode_lies_in_dimensions(antinode_x, antinode_y, dimensions):
        antinode_list.append((antinode_x, antinode_y))
        antinode_x += m_x
        antinode_y += m_y

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
    print(evaluate_input_part_2(input_data, dimensions))

if __name__ == "__main__":
    main()
