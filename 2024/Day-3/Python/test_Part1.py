import unittest
from Part1 import evaluate_mul_operations

class TestEvaluateMulOperations(unittest.TestCase):
    def test_evaluate_mul_operations(self):
        input_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        expected_result = 161  # 2*4 + 5*5 + 11*8 + 8*5
        self.assertEqual(evaluate_mul_operations(input_string), expected_result)

if __name__ == '__main__':
    unittest.main()
