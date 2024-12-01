file_path = '2024\Day 1\input.txt'

def read_input():
    # Open the file
    with open(file_path) as file:
        # Define the two lists
        list1 = []
        list2 = []
        # Iterate through the lines
        for line in file:
            # Split the line
            split_line = line.split()
            # Add the first integer to list1
            list1.append(int(split_line[0]))
            # Add the second integer to list2
            list2.append(int(split_line[1]))
    # Return the two lists
    return list1, list2
