import unittest
from Util import read_input
from Part1 import evaluate_input


class TestDay8(unittest.TestCase):
    def test_evaluate_input_simple(self):
        test_input, test_dimensions = read_input("2024/Day-8/test_input_simple.txt")
        test_result = 2
        self.assertEqual(evaluate_input(test_input, test_dimensions), test_result)

    def test_evaluate_input_case_2(self):
        test_input, test_dimensions = read_input("2024/Day-8/test_input_case_2.txt")
        test_result = 4
        self.assertEqual(evaluate_input(test_input, test_dimensions), test_result)

    def test_evaluate_input_case_3(self):
        test_input, test_dimensions = read_input("2024/Day-8/test_input_case_3.txt")
        test_result = 4
        self.assertEqual(evaluate_input(test_input, test_dimensions), test_result)

    def test_evaluate_input_case_4(self):
        test_input, test_dimensions = read_input("2024/Day-8/test_input_case_4.txt")
        test_result = 14
        self.assertEqual(evaluate_input(test_input, test_dimensions), test_result)


if __name__ == '__main__':
    unittest.main()
