import unittest
from Util import read_input
from Part1 import evaluate_input

class TestDay9(unittest.TestCase):
    def test_evaluate_input_simple(self):
        test_input, test_coords = read_input("2024/Day-10/test_input.txt")
        test_result = 1
        self.assertEqual(evaluate_input(test_input, test_coords), test_result)

    def test_evaluate_input_2(self):
        test_input, test_coords = read_input("2024/Day-10/test_input_2.txt")
        test_result = 2
        self.assertEqual(evaluate_input(test_input, test_coords), test_result)

    def test_evaluate_input_3(self):
        test_input, test_coords = read_input("2024/Day-10/test_input_3.txt")
        test_result = 4
        self.assertEqual(evaluate_input(test_input, test_coords), test_result)

    def test_evaluate_input_4(self):
        test_input, test_coords = read_input("2024/Day-10/test_input_4.txt")
        test_result = 3
        self.assertEqual(evaluate_input(test_input, test_coords), test_result)

    def test_evaluate_input_5(self):
        test_input, test_coords = read_input("2024/Day-10/test_input_5.txt")
        test_result = 36
        self.assertEqual(evaluate_input(test_input, test_coords), test_result)

    # def test_evaluate_input_part_2(self):
    #     test_input = read_input("2024/Day-10/test_input.txt")
    #     test_result = 2858
    #     self.assertEqual(evaluate_input_part_2(test_input), test_result)


if __name__ == '__main__':
    unittest.main()
