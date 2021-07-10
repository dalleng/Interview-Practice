import unittest
from typing import List


class Solution:
    def twoSumClosest(self, nums, start, target):
        lo = start
        hi = len(nums) - 1
        closest = None

        while lo < hi:
            if lo != start and nums[lo] == nums[lo - 1]:
                lo += 1
                continue

            if closest is None:
                closest = nums[lo] + nums[hi]
            elif abs(target - (nums[lo] + nums[hi])) < abs(target - closest):
                closest = nums[lo] + nums[hi]

            if nums[lo] + nums[hi] == target:
                return nums[lo] + nums[hi]
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                lo += 1

        return closest

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = None
        nums.sort()
        print(f"sorted nums: {nums}")

        for i, n in enumerate(nums):
            print(f"i:{i} n:{n}")
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ret = self.twoSumClosest(nums, i + 1, target - n)
            print(f"ret: {ret}")

            if closest is None:
                closest = n + ret

            if ret and n + ret == target:
                return n + ret
            elif ret and abs(target - (n + ret)) < abs(target - closest):
                closest = n + ret
            print(f"closest: {closest}")

        return closest


class ThreeSumClosest(unittest.TestCase):

    def test_basic(self):
        got = Solution().threeSumClosest([-1, 2, 1, -4], 1)
        self.assertEqual(got, 2)

    def test_basic2(self):
        got = Solution().threeSumClosest([0, 2, 1, -3], 1)
        self.assertEqual(got, 0)

    def test_exact_solution_at_the_start(self):
        got = Solution().threeSumClosest([1, 2, 3], 6)
        self.assertEqual(got, 6)

    def test_exact_solution_at_the_end(self):
        got = Solution().threeSumClosest([0, 0, 0, 0, 1, 2, 3], 6)
        self.assertEqual(got, 6)

    def test_large_negative_numbers(self):
        got = Solution().threeSumClosest([-100, -98, -2, -1], -101)
        self.assertEqual(got, -101)


if __name__ == '__main__':
    print()
    unittest.main()
