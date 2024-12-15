input_file = "2024/Day-11/input.txt"

def read_input(file_path=input_file):
    out = []
    zero_coords = []
    with open(file_path, "r") as file:
        i = 0
        for line in file:
            line_arr = []
            for j, c in enumerate(line.strip().strip("\n")):
                if c == '0':
                    zero_coords.append((i, j))
                try:
                    line_arr.append(int(c))
                except:
                    line_arr.append(c)
            out.append(line_arr)
            i += 1
    return out, zero_coords
