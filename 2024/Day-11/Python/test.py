import unittest
from Util import read_input
from Part1 import evaluate_input
from Part2 import evaluate_input_part_2

class TestDay11(unittest.TestCase):
    def test_evaluate_input_simple(self):
        test_input = read_input("2024/Day-11/test_input/p1_1.txt")
        test_result = 7
        self.assertEqual(evaluate_input(test_input), test_result)

    def test_evaluate_stone_rules(self):
        test_input = read_input("2024/Day-11/test_input/p1_1.txt")
        test_result = [1, 2024, 1, 0, 9, 9, 2021976]
        evaluate_input(test_input)
        self.assertEqual(test_input, test_result)

    def test_evaluate_stone_rules_large(self):
        test_input = read_input("2024/Day-11/test_input/p1_2.txt")
        test_result = [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2] # given from prompt after six blinks
        evaluate_input(test_input, 6)
        self.assertEqual(test_input, test_result)


if __name__ == '__main__':
    unittest.main()
