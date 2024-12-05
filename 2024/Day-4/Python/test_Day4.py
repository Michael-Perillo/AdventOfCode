import unittest
from Part1 import count_xmas_occurrences
from Part2 import count_x_shaped_mas_occurrences


class TestDay4(unittest.TestCase):
    def test_count_xmas_occurrences_given(self):
        test_input = [
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX"]
        expected_result = 18  # Given from the prompt
        self.assertEqual(count_xmas_occurrences(test_input), expected_result)

    def test_count_xmas_occurrences_single(self):
        test_input = [
            "...XMAS...",
            "..........",
            "..........",
            ".........."]
        expected_result = 1  # Given from the prompt
        self.assertEqual(count_xmas_occurrences(test_input), expected_result)

    def test_count_xmas_occurrences_single_backwards(self):
        test_input = [
            "...SAMX...",
            "..........",
            "..........",
            ".........."]
        expected_result = 1  # Given from the prompt
        self.assertEqual(count_xmas_occurrences(test_input), expected_result)

    def test_count_x_shaped_mas_occurrences_given(self):
        test_input = [
            ".M.S......",
            "..A..MSMS.",
            ".M.S.MAA..",
            "..A.ASMSM.",
            ".M.S.M....",
            "..........",
            "S.S.S.S.S.",
            ".A.A.A.A..",
            "M.M.M.M.M.",
            ".........."]
        expected_result = 9
        self.assertEqual(count_x_shaped_mas_occurrences(test_input), expected_result)

    def test_count_x_shaped_mas_occurrences_simple(self):
        test_input = [
            "M.S",
            ".A.",
            "M.S",
            ]
        expected_result = 1
        self.assertEqual(count_x_shaped_mas_occurrences(test_input), expected_result)



if __name__ == '__main__':
    unittest.main()
