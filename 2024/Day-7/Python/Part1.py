from Util import read_input
import itertools

# Given the dictionary of inputs, where the keys are the results and the values are the inputs, determine if the result
# is the sum/product of the inputs.
# The inputs are evaluated left to right, regardless of the order of operations.
# The inputs can either be added or multiplied.

def evaluate_input(input_dict):
    # evaluate each input in the dictionary
    # return the sum of the results that match the criteria
    valid_results = []
    for result, inputs in input_dict.items():
        if evaluate_expression_brute_force(result, inputs):
            valid_results.append(result)
    print(len(valid_results))
    sum_ = 0
    for i in range(len(valid_results)):
        print(f"{i}: {valid_results[i]} + {sum_} = {valid_results[i] + sum_}")
        sum_ += valid_results[i]
    print(type(valid_results))
    return sum(valid_results)

def evaluate_expression_from_back(result, inputs):
    if len(inputs) == 1:
        return result - inputs[0] == 0
    else:
        # check if the result is divisible by the last element
        if result % inputs[-1] == 0:
            return evaluate_expression_from_back(result // inputs[-1], inputs[:-1])
        # otherwise, subtract the last element from the result and continue
        return evaluate_expression_from_back(result - inputs[-1], inputs[:-1])


def evaluate_expression(result, inputs):
    # determine if the result is the sum or product of the inputs
    # evaluate the expression left to right
    if len(inputs) == 1:
        return result == inputs[0]
    else:
        sum_list = [inputs[0] + inputs[1]] + inputs[2:]
        product_list = [inputs[0] * inputs[1]] + inputs[2:]
        if evaluate_expression(result, sum_list):
            return True
        elif evaluate_expression(result, product_list):
            return True
    return False

def evaluate_expression_iterative(result, inputs):
    # Use a stack to simulate the evaluation process
    stack = [(inputs, 0)]  # (current list of inputs, current index)

    while stack:
        current_inputs, index = stack.pop()

        # If we have reduced the inputs to a single element, check if it matches the result
        if len(current_inputs) == 1:
            if current_inputs[0] == result:
                return True
            continue

        # Evaluate the sum and product of the current pair of elements
        if index < len(current_inputs) - 1:
            sum_list = current_inputs[:index] + [current_inputs[index] + current_inputs[index + 1]] + current_inputs[index + 2:]
            product_list = current_inputs[:index] + [current_inputs[index] * current_inputs[index + 1]] + current_inputs[index + 2:]

            # Push the new lists onto the stack for further evaluation
            stack.append((sum_list, 0))
            stack.append((product_list, 0))

    return False

def generate_operator_combinations(length):
    operators = ['+', '*']
    return list(itertools.product(operators, repeat=length))

def evaluate_expression_given_operator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '*':
        return a * b

def evaluate_inputs_given_operators(inputs, operators):
    result = inputs[0]
    for i in range(len(operators)):
        result = evaluate_expression_given_operator(result, inputs[i + 1], operators[i])
    return result

def evaluate_expression_brute_force(result, inputs):
    num_operators = len(inputs) - 1
    # Generate all possible combinations of operators
    operator_combinations = generate_operator_combinations(num_operators)
    # evaluate the list of inputs with each operator combination
    for operators in operator_combinations:
        if evaluate_inputs_given_operators(inputs, operators) == result:
            return True
    return False

def pretty_print(input_dict):
    i = 0
    for result, inputs in input_dict.items():
        i += 1
        print(f"{i}: {result} = {' + '.join([str(i) for i in inputs])}")

def main():
    # Read the input file
    input_data = read_input()
    # print(len(input_data))
    # pretty_print(input_data)
    # Evaluate the input data
    print(evaluate_input(input_data))

if __name__ == "__main__":
    main()
