from Util import read_input


def evaluate_input(input_data, storage_size):
    # Generate a list representing the final storage
    # as we generate the list, insert the files from the end of the storage as we encounter them
    storage = []
    last_file_id = len(input_data) - 1
    for i in range(len(input_data)):
        file_size, free_space = input_data[i]
        for j in range(file_size):
            storage.append(i)
            input_data[i] = (file_size - 1, free_space)
        if i == last_file_id:
            break
        for j in range(free_space):
            # get the last file ID from the storage
            final_element_size, _ = input_data[last_file_id]
            # check if the final element still has size
            if final_element_size == 0:
                last_file_id -= 1
                final_element_size, _ = input_data[last_file_id]
            # insert the file ID after the current file ID
            storage.append(last_file_id)
            # decrement the size of the final element
            input_data[last_file_id] = (final_element_size - 1, _)
    return storage

def calculate_checksum(storage):
    output = 0
    for i in range(len(storage)):
        if storage[i] == '.':
            continue
        output += int(storage[i]) * i
    return output


def main():
    # Read the input file
    input_data, storage_size = read_input()
    print(calculate_checksum(evaluate_input(input_data, storage_size)))

if __name__ == "__main__":
    main()
