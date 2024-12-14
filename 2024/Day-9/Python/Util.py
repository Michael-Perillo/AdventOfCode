input_file = "2024/Day-9/input.txt"

def read_input(file_path=input_file):
    storage_size = 0
    with open(file_path, "r") as file:
        file_content = file.read().strip().strip("\n")
        # split the file content every two characters
        file_sizes = [file_content[i:i+2] for i in range(0, len(file_content), 2)]
        # convert the file sizes to a dictionary of ID: (size, free_space) key-value pairs
        out = {}
        for i in range(len(file_sizes)):
            if len(file_sizes[i]) < 2:
                out[i] = (int(file_sizes[i]), 0)
                continue
            file_size, free_space = int(file_sizes[i][0]), int(file_sizes[i][1])
            storage_size += file_size + free_space
            out[i] = (file_size, free_space)
    return out, storage_size
