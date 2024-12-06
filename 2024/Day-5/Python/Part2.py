from Util import read_input
from Part1 import sum_of_middle_digits, is_correct_order

# Part 2: Determine which updates are not in the correct order, correct them, and return the sum of their middle digits

def get_corrected_messages(ordering, messages):
    # we want to return the sum of the middle digits of the messages that are in the correct order
    # we can determine the correct order by checking the ordering dictionary
    correct_ordered_messages = []
    for message in messages:
        if not is_correct_order(ordering, message):
            correct_ordered_messages.append(correct_message(ordering, message))
    return correct_ordered_messages

def correct_message(ordering, message):
    # for each digit in the message:
    # check all digits that come before it
    # if any of those digits are in the ordering dictionary for the current digit, then the message is not in the correct order
    corrected_message = message.copy()
    i = 1
    while i < len(corrected_message):
        current_digit = corrected_message[i]
        if ordering.get(current_digit) is not None:
            current_ordering = ordering[current_digit]
            for j in range(i):
                compare_digit = corrected_message[j]
                if compare_digit in current_ordering:
                    # move the j digit to the position after the i digit
                    corrected_message.insert(i, corrected_message.pop(j))
                    # restart the loop
                    i = 0
                    break
        i += 1
    return corrected_message


def main():
    ordering, messages = read_input()
    print(sum_of_middle_digits(get_corrected_messages(ordering, messages)))

if __name__ == "__main__":
    main()
