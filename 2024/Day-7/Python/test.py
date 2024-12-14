import unittest
from Util import read_input
from Part1 import evaluate_expression, evaluate_input, evaluate_expression_iterative, evaluate_expression_from_back, evaluate_expression_brute_force


class TestDay7(unittest.TestCase):
    def test_evaluate_input_simple(self):
        test_input = [10, 19]
        test_result = 190
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input_complex(self):
        test_input = [81, 40, 27]
        test_result = 3267
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input_complex_2(self):
        test_input = [11, 6, 16, 20]
        test_result = 292
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input_new(self):
        test_input = [26, 37, 33, 56, 79, 42, 60, 33]
        test_result = 40656
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input_new_1(self):
        test_input = [46, 62, 81, 97, 72]
        test_result = 20592
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input_new_2(self):
        test_input = [23, 47, 69, 82, 69, 83, 41]
        test_result = 39022201
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input_new_3(self):
        test_input = [73, 91, 24, 78, 75, 93, 11, 36, 42, 86, 25, 24, 66, 26]
        test_result = 536008016
        self.assertTrue(evaluate_expression_brute_force(test_result, test_input))

    # def test_evaluate_input_new_4(self):
    #     test_input = [5, 1, 2]
    #     test_result = 5
    #     self.assertTrue(evaluate_expression(test_result, test_input))

    def test_single_input(self):
        self.assertTrue(evaluate_expression_brute_force(5, [5]))
        self.assertFalse(evaluate_expression_brute_force(5, [3]))

    def test_sum_of_two_inputs(self):
        self.assertTrue(evaluate_expression_brute_force(5, [2, 3]))
        self.assertFalse(evaluate_expression_brute_force(5, [2, 2]))

    def test_product_of_two_inputs(self):
        self.assertTrue(evaluate_expression_brute_force(6, [2, 3]))
        self.assertFalse(evaluate_expression_brute_force(6, [2, 2]))

    def test_sum_and_product_of_multiple_inputs(self):
        self.assertTrue(evaluate_expression_brute_force(11, [2, 3, 6]))
        self.assertTrue(evaluate_expression_brute_force(12, [2, 3, 2]))
        self.assertTrue(evaluate_expression_brute_force(10, [2, 3, 4]))

    def test_complex_case(self):
        self.assertTrue(evaluate_expression_brute_force(41, [1, 2, 3, 4, 5]))
        self.assertFalse(evaluate_expression_brute_force(20, [1, 2, 3, 4, 5]))

    def test_evaluate_input_false(self):
        test_input = [9, 7, 18, 13]
        test_result = 21037
        self.assertFalse(evaluate_expression_brute_force(test_result, test_input))

    def test_evaluate_input(self):
        test_input = read_input("2024/Day-7/test_input.txt")
        self.assertEqual(evaluate_input(test_input), 190 + 3267 + 292)



if __name__ == '__main__':
    unittest.main()
