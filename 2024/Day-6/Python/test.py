import unittest
from Util import read_input
from Part1 import count_distinct_positions


class TestDay6(unittest.TestCase):
    def test_read_input(self):
        expected_result = [
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
        self.assertEqual(read_input("2024/Day-6/test_input.txt"), expected_result)

    def test_count_distinct_positions(self):
        test_map = read_input("2024/Day-6/test_input.txt")
        expected_result = 41  # Given from the prompt
        self.assertEqual(count_distinct_positions(test_map), expected_result)



if __name__ == '__main__':
    unittest.main()
