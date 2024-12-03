from Util import read_input
from Part1 import evaluate_mul_operations
import re

# Part Two:
# There are two new instructions you'll need to handle:

# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

def evaluate_conditioned_mul_operations(input_string):
    # define a regex pattern to find all the disabled data
    disabled_pattern = r"don't\(\).*?(do\(\)|$)"
    # remove the disabled data
    input_string_clean = re.sub(disabled_pattern, "", input_string, flags=re.DOTALL)
    print(input_string_clean)
    return evaluate_mul_operations(input_string_clean)


def main():
    input_string = read_input()
    print(evaluate_conditioned_mul_operations(input_string))

if __name__ == "__main__":
    main()
