input_file = "2024/Day-11/input.txt"

def read_input(file_path=input_file):
    with open(file_path, "r") as file:
        file_content = file.read().strip().strip("\n")
        return [int(i) for i in file_content.split()]
