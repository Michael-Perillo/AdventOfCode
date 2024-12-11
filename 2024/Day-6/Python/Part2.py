from Util import read_input
from Part1 import get_next_position, turn_right, get_correct_range

# Part 2: Given the same map and starting position, determine the number of positions where placing an object will cause the guard to loop infinitely.
#

def check_if_loop(loop_positions, guard_map, visited_positions, direction, i, j):
    possible_position = is_obstacle_to_right(guard_map, direction, i, j)
    if possible_position:
        # if we have an obstacle to the right, and turning here would intersect the previous path, then we have a loop
        if visited_positions.get(possible_position, False) and possible_position != (i, j):
            loop_positions.append((i, j))

def has_exited(guard_map, position):
    i, j = position
    return i == 0 or i == len(guard_map) - 1 or j == 0 or j == len(guard_map[0]) - 1

def is_obstacle_to_right(guard_map, direction, i, j):
    # Given the map, direction, and the current position, determine if there is an obstacle to the right
    possible_position = get_next_position(guard_map, (i, j), turn_right(direction))
    if not has_exited(guard_map, possible_position):
        return possible_position
    return ()


def find_loops_and_update_visited_positions(guard_map, visited_positions, direction, current_position, next_position):
    # Given the current position, the next position, and the visited positions, update the visited positions
    # and return the positions where the guard has looped
    i, j = current_position
    i_next, j_next = next_position
    loop_positions = []
    # if the guard intersects the previous path AND there is a wall to the right, then we have a loop
    # update the visited positions
    for k in get_correct_range(i, i_next):
        visited_positions[(k, j)] = True
        check_if_loop(loop_positions, guard_map, visited_positions, direction, k, j)
    for k in get_correct_range(j, j_next):
        visited_positions[(i, k)] = True
        check_if_loop(loop_positions, guard_map, visited_positions, direction, i, k)
    return visited_positions, loop_positions

def count_loop_positions(guard_map, starting_position):
    # if we intersect our previous path AND there is a wall if we turn right, then we have a loop

        # Initialize a dictionary to keep track of the visited positions
    visited_positions = {}
    # Initialize a list to keep track of the loop positions
    loop_positions = []
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
        # during the update, check if the current path intersects with the previous paths
        visited_positions, temp_loop_positions = find_loops_and_update_visited_positions(guard_map, visited_positions, direction, current_position, next_position)
        # if we have a loop, add the loop positions to the list of loop positions
        if temp_loop_positions:
            loop_positions.extend(temp_loop_positions)
        # update the current position
        current_position = next_position
        # update the coordinates
        i, j = current_position
    # return the number of distinct positions visited
    return len(loop_positions)


    # the obstacles can be thought of as corners of a rectangle
    # the guard will loop infinitely if the rectangle is completed
    # we need to find the number of positions where placing an object will complete the rectangle
    # basically we need to do the same thing as part 1, but we need to keep track of the paths the guard has taken
    # Then check if the current path intersects with the previous paths
    # I believe there is only one path that could intersect with the current path, would be current path - 3
    #
    # Start by generating the paths the guard has taken
    # represent the path as a list of coordinate pairs, where each pair is the starting and ending position of the path

    paths = []
    current_position = starting_position
    direction = "up"

    i, j = current_position




    # If they do, then we have a loop



def main():
    # Read the input
    guard_map, starting_position = read_input()
    # count the number of positions where placing an object will cause the guard to loop infinitely
    num_loops = count_loop_positions(guard_map, starting_position)
    print(num_loops)

if __name__ == '__main__':
    main()
