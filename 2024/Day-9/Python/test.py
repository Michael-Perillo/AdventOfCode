import unittest
from Util import read_input
from Part1 import evaluate_input, calculate_checksum
from Part2 import evaluate_input_part_2

class TestDay9(unittest.TestCase):
    def test_evaluate_input_simple(self):
        test_input, size = read_input("2024/Day-9/test_input.txt")
        test_result = 1928
        self.assertEqual(calculate_checksum(evaluate_input(test_input, size)), test_result)

    def test_evaluate_input_part_2(self):
        test_input, size = read_input("2024/Day-9/test_input.txt")
        test_result = 2858
        self.assertEqual(calculate_checksum(evaluate_input_part_2(test_input)), test_result)


if __name__ == '__main__':
    unittest.main()
