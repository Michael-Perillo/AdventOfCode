from Util import read_input

# Part 1: Given a map and an initial starting position, determine the number of distinct positions that are reached
# the guard can move only in the direction they are facing, initially up
# If there is a wall in the direction they are facing, they turn right 90 degrees and continue
# Eventually the guard should exit the map

def turn_right(direction):
    # Given the current direction, return the new direction after turning right
    if direction == "up":
        return "right"
    elif direction == "right":
        return "down"
    elif direction == "down":
        return "left"
    elif direction == "left":
        return "up"

def get_next_position(guard_map, current_position, direction):
    # Get the current position's coordinates
    i, j = current_position
    # Determine the next position based on the direction by incrementing the coordinates until a wall is reached
    if direction == "up":
        while i > 0 and guard_map[i - 1][j] != "#":
            i -= 1
    elif direction == "down":
        while i < len(guard_map) - 1 and guard_map[i + 1][j] != "#":
            i += 1
    elif direction == "left":
        while j > 0 and guard_map[i][j - 1] != "#":
            j -= 1
    elif direction == "right":
        while j < len(guard_map[0]) - 1 and guard_map[i][j + 1] != "#":
            j += 1
    return (i, j)

def update_visited_positions(visited_positions, current_position, next_position):
    # Given the current position and the next position, update the visited positions dictionary
    i, j = current_position
    i_next, j_next = next_position
    for k in get_correct_range(i, i_next):
        visited_positions[(k, j)] = True
    for k in get_correct_range(j, j_next):
        visited_positions[(i_next, k)] = True
    return visited_positions

def get_correct_range(i, i_next):
    # return the range of coordinates depending on which is greater
    if i < i_next:
        return range(i, i_next + 1)
    else:
        return range(i_next, i + 1)

def count_distinct_positions(guard_map, starting_position):
    # Initialize a dictionary to keep track of the visited positions
    visited_positions = {}
    # Initialize the current position
    current_position = starting_position
    # initialize the starting position as visited
    visited_positions[current_position] = True
    # initialize the coordinates to begin iterating
    i, j = current_position
    # initialize the direction the guard is facing
    direction = "up"
    has_exited = False
    # iterate until the guard exits the map
    while not has_exited:
        # determine the next position
        next_position = get_next_position(guard_map, current_position, direction)
        # if the next position is a wall, turn right
        if next_position == current_position:
            direction = turn_right(direction)
            continue
        # if the next position is outside the map, exit
        if i == 0 or i == len(guard_map) - 1 or j == 0 or j == len(guard_map[0]) - 1:
            has_exited = True
            break
        # mark all positions between the current position and the next position as visited
        visited_positions = update_visited_positions(visited_positions, current_position, next_position)
        # update the current position
        current_position = next_position
        # update the coordinates
        i, j = current_position
    # return the number of distinct positions visited
    return len(visited_positions)


def main():
    guard_map, starting_position = read_input()
    print(count_distinct_positions(guard_map, starting_position))

if __name__ == "__main__":
    main()
