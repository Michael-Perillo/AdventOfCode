import unittest
from Util import read_input
from Part1 import sum_of_middle_digits, is_correct_order



class TestDay5(unittest.TestCase):
    def test_sum_of_middle_digits(self):
        test_ordering, test_messages = read_input("2024/Day-5/test_input.txt")
        expected_result = 143  # Given from the prompt
        self.assertEqual(sum_of_middle_digits(test_ordering, test_messages), expected_result)

    def test_is_correct_order(self):
        test_ordering, _ = read_input("2024/Day-5/test_input.txt")
        test_message = [75,47,61,53,29]
        self.assertTrue(is_correct_order(test_ordering, test_message))



if __name__ == '__main__':
    unittest.main()
