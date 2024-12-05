from Util import read_input

# Part 1: Determine which updates are in the correct order from the given input, return the sum of their middle digits

def main():
    ordering, messages = read_input()
    print(sum_of_middle_digits(ordering, messages))

def sum_of_middle_digits(ordering, messages):
    # we want to return the sum of the middle digits of the messages that are in the correct order
    # we can determine the correct order by checking the ordering dictionary
    correct_ordered_messages = []
    for message in messages:
        if is_correct_order(ordering, message):
            correct_ordered_messages.append(message)
    return sum([message[len(message)//2] for message in correct_ordered_messages])

def is_correct_order(ordering, message):
    # for each digit in the message:
    # check all digits that come before it
    # if any of those digits are in the ordering dictionary for the current digit, then the message is not in the correct order
    for i in range(1, len(message)):
        if ordering.get(message[i]) is not None:
            for j in range(i):
                if message[j] in ordering[message[i]]:
                    return False
    return True







if __name__ == "__main__":
    main()
