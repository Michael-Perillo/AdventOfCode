from Util import read_input
from Part1 import calculate_checksum

# This time, attempt to move whole files to the leftmost span of free space blocks that could fit the file. Attempt to move each file exactly once in order of decreasing file ID number starting with the file with the highest file ID number. If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.

# The checksum is calculated as before, but using the new storage configuration.

def evaluate_input_part_2(input_data):
    # Generate a list representing the final storage
    # generate the list by iterating over the input data from the end
    # insert the files at the leftmost span of free space blocks that could fit the file
    # to do this, augment the input data with a list of free space blocks
    augmented_input_data = augment_input_data(input_data)
    last_file_id = len(input_data) - 1
    for i in range(last_file_id, -1, -1):
        file_size, _, _ = augmented_input_data[i]
        for j in range(i):
            _, free_space_remaining, free_space_contents = augmented_input_data[j]
            if file_size <= free_space_remaining:
                free_space_start = len(free_space_contents) - free_space_remaining
                for k in range(file_size):
                    augmented_input_data[j] = (augmented_input_data[j][0], augmented_input_data[j][1] - 1, augmented_input_data[j][2])
                    augmented_input_data[j][2][free_space_start + k] = i
                    augmented_input_data[i] = (0, 0, ['.'] + (augmented_input_data[i][2]))
                break
    return generate_storage(augmented_input_data)

def generate_storage(augmented_input_data):
    storage = []
    for file_id, (file_size, _, free_space_contents) in augmented_input_data.items():
        for i in range(file_size):
            storage.append(file_id)
        for item in free_space_contents:
            storage.append(item)
    return storage

def augment_input_data(input_data):
    # add a list for all free space blocks based on the input data
    augmented_input_data = {}
    for file_id, (file_size, free_space) in input_data.items():
        augmented_input_data[file_id] = (file_size, free_space, ['.' for _ in range(free_space)])
    return augmented_input_data

def main():
    # Read the input file
    input_data, _ = read_input()
    print(calculate_checksum(evaluate_input_part_2(input_data)))

if __name__ == "__main__":
    main()
