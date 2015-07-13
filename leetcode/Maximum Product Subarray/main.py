import unittest


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        current_max = nums[0]
        current_min = nums[0]
        max_prod = nums[0]
        for n in nums[1:]:
            tmp = current_max
            current_max = max(n, n*current_max, n*current_min)
            current_min = min(n, n*tmp, n*current_min)
            max_prod = max(max_prod, current_max)
        return max_prod


class MaxProductTest(unittest.TestCase):
    def test_single(self):
        self.assertEquals(Solution().maxProduct([0]), 0)
        self.assertEquals(Solution().maxProduct([1]), 1)

    def test_list(self):
        self.assertEquals(Solution().maxProduct([1, 2, -3, 8, 9]), 72)
        self.assertEquals(Solution().maxProduct([1, 2, -3, 0]), 2)
        self.assertEquals(Solution().maxProduct([0, 0, 4, 2, -2]), 8)
        self.assertEquals(Solution().maxProduct([-1, 0]), 0)
        self.assertEquals(Solution().maxProduct([-2, 3, -4]), 24)
        self.assertEquals(Solution().maxProduct([2, -5, -2, -4, 3]), 24)

    def test_all_negative(self):
        self.assertEquals(Solution().maxProduct([-1, -2, -3]), 6)


if __name__ == '__main__':
    unittest.main()
