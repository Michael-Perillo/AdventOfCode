from Util import read_input
import re

# Part 1: Given a string as input, extract the multiplication operations and evaluate them. Return the sum of the results.
# definition of multiplication operations within the string: mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.
# there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

def evaluate_mul_operations(input_string):
    # use regex to find all the multiplication operations
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", input_string)
    # use a list comprehension to evaluate each operation
    return sum([int(x) * int(y) for x, y in multiplications])


def main():
    input_string = read_input()
    print(evaluate_mul_operations(input_string))

if __name__ == "__main__":
    main()
