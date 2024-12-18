from Util import read_input
from functools import cache

def evaluate_input_part_2(input_data, blinks = 1):

    @cache
    def evaluate_stone_recursive(stone: str, blinks: int) -> int:
        if blinks == 0:
            return 1
        if stone == '0':
            return evaluate_stone_recursive('1', blinks-1)
        if len(stone) % 2 == 0:
            # Calculate the midpoint
            midpoint = len(stone) // 2
            # Get the first half and convert it back to an integer
            first_half = int(stone[:midpoint])
            # Get the second half and convert it back to an integer
            second_half = int(stone[midpoint:])
            # Replace the original element with the two new elements
            return evaluate_stone_recursive(str(first_half), blinks-1) + evaluate_stone_recursive(str(second_half), blinks-1)
        return evaluate_stone_recursive(str(int(stone) * 2024), blinks-1)

    return sum([evaluate_stone_recursive(str(stone), blinks) for stone in input_data])

def main():
    # Read the input file
    input_data = read_input()
    print((evaluate_input_part_2(input_data, 75)))

if __name__ == "__main__":
    main()
