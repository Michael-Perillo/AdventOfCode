import unittest
from Part2 import is_safe_with_level_remove

class TestIsSafe(unittest.TestCase):
    def test_is_safe(self):
        # Test cases
        self.assertTrue(is_safe_with_level_remove([7, 6, 4, 2, 1]))  # Safe without removing any level
        self.assertFalse(is_safe_with_level_remove([1, 2, 7, 8, 9]))  # Unsafe regardless of which level is removed
        self.assertFalse(is_safe_with_level_remove([9, 7, 6, 2, 1]))  # Unsafe regardless of which level is removed
        self.assertTrue(is_safe_with_level_remove([1, 3, 2, 4, 5]))  # Safe by removing the second level, 3
        self.assertTrue(is_safe_with_level_remove([8, 6, 4, 4, 1]))  # Safe by removing the third level, 4
        self.assertTrue(is_safe_with_level_remove([1, 3, 6, 7, 9]))  # Safe without removing any level

if __name__ == '__main__':
    unittest.main()
