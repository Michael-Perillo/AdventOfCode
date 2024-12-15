from Util import read_input

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
def evaluate_stone_rules(input_data, blinks=1):
    for blink in range(blinks):
        i = 0
        length = len(input_data)
        while True:
            if input_data[i] == 0:
                input_data[i] = 1
                i += 1
            elif len(str(input_data[i])) % 2 == 0:
                # Convert the integer to a string
                str_value = str(input_data[i])
                # Calculate the midpoint
                midpoint = len(str_value) // 2
                # Get the first half and convert it back to an integer
                first_half = int(str_value[:midpoint])
                # Get the second half and convert it back to an integer
                second_half = int(str_value[midpoint:])
                # Replace the original element with the two new elements
                input_data[i:i+1] = [first_half, second_half]
                i += 2
            else:
                input_data[i] *= 2024
                i += 1
            length = len(input_data)
            if i >= length:
                break
    return

def evaluate_input(input_data, blinks=1):
    evaluate_stone_rules(input_data, blinks)
    return len(input_data)

def main():
    # Read the input file
    input_data = read_input()
    print(evaluate_input(input_data, 25))

if __name__ == "__main__":
    main()
