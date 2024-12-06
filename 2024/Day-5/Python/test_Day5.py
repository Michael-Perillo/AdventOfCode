import unittest
from Util import read_input
from Part1 import sum_of_middle_digits, is_correct_order, get_correct_messages
from Part2 import correct_message



class TestDay5(unittest.TestCase):
    def test_sum_of_middle_digits(self):
        test_ordering, test_messages = read_input("2024/Day-5/test_input.txt")
        expected_result = 143  # Given from the prompt
        self.assertEqual(sum_of_middle_digits(get_correct_messages(test_ordering, test_messages)), expected_result)

    def test_is_correct_order(self):
        test_ordering, _ = read_input("2024/Day-5/test_input.txt")
        test_message = [75,47,61,53,29]
        self.assertTrue(is_correct_order(test_ordering, test_message))

    def test_get_correct_messages_1(self):
        test_ordering, _ = read_input("2024/Day-5/test_input.txt")
        test_message = [75,97,47,61,53]
        expected_result = [97,75,47,61,53]
        self.assertEqual(correct_message(test_ordering, test_message), expected_result)

    def test_get_correct_messages_2(self):
        test_ordering, _ = read_input("2024/Day-5/test_input.txt")
        test_message = [61,13,29]
        expected_result = [61,29,13]
        self.assertEqual(correct_message(test_ordering, test_message), expected_result)

    def test_get_correct_messages_3(self):
        test_ordering, _ = read_input("2024/Day-5/test_input.txt")
        test_message = [97,13,75,29,47]
        expected_result = [97,75,47,29,13]
        self.assertEqual(correct_message(test_ordering, test_message), expected_result)



if __name__ == '__main__':
    unittest.main()
