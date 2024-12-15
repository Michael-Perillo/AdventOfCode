import unittest
from Util import read_input
from Part1 import evaluate_input
from Part2 import evaluate_input_part_2

class TestDay9(unittest.TestCase):
    def test_evaluate_input_simple(self):
        test_input = read_input("2024/Day-11/test_input/p1_1.txt")
        test_result = 1
        self.assertEqual(evaluate_input(test_input), test_result)


if __name__ == '__main__':
    unittest.main()
