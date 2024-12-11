import unittest
from Util import read_input
from Part1 import count_distinct_positions
from Part2 import count_loop_positions

class TestDay6(unittest.TestCase):
    def test_read_input(self):
        expected_result_map = [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#..."
        ]
        expected_result_starting_position = (6, 4)
        expected_result = (expected_result_map, expected_result_starting_position)
        self.assertEqual(read_input("2024/Day-6/test_input.txt"), expected_result)

    def test_count_distinct_positions(self):
        test_map, test_starting_position = read_input("2024/Day-6/test_input.txt")
        expected_result = 41  # Given from the prompt
        self.assertEqual(count_distinct_positions(test_map, test_starting_position), expected_result)

    def test_count_loop_positions(self):
        test_map, test_starting_position = read_input("2024/Day-6/test_input.txt")
        expected_result = 6 # Given from the prompt
        self.assertEqual(count_loop_positions(test_map, test_starting_position), expected_result)



if __name__ == '__main__':
    unittest.main()
