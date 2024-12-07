import os
import re

file_path = "2024/Day-6/Input.txt"

def read_input(input_file_path=file_path):
    out = []
    with open(input_file_path, "r") as file:
        for line in file:
            if line.strip() == "":
                continue
            out.append(line.strip())
