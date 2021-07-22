import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        si = self.findSmallestIndex(nums)

        if nums[si] == target:
            return si

        rl = None
        if si > 0:
            rl = self.binarySearch(nums, target, 0, si - 1)

        if rl is not None:
            return rl

        rr = None
        if si < len(nums) - 1:
            rr = self.binarySearch(nums, target, si + 1, len(nums) - 1)

        if rr is not None:
            return rr

        return -1

    def binarySearch(self, nums, target, lo, hi):
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

    def findSmallestIndex(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                return mid
            elif nums[hi] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1


class TestSearch(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(Solution().search([8], 8), 0)

    def test_single_element_no_target_found(self):
        self.assertEqual(Solution().search([8], 9), -1)

    def test_pivot_0(self):
        nums = list(map(int, '0124567'))
        for i, n in enumerate(nums):
            with self.subTest(n=n, i=i):
                self.assertEqual(Solution().search(nums, n), i)

    def test_pivot_1(self):
        nums = list(map(int, '1245670'))
        for i, n in enumerate(nums):
            with self.subTest(n=n, i=i):
                self.assertEqual(Solution().search(nums, n), i)

    def test_pivot_2(self):
        nums = list(map(int, '2456701'))
        for i, n in enumerate(nums):
            with self.subTest(n=n, i=i):
                self.assertEqual(Solution().search(nums, n), i)

    def test_pivot_3(self):
        nums = list(map(int, '4567012'))
        for i, n in enumerate(nums):
            with self.subTest(n=n, i=i):
                self.assertEqual(Solution().search(nums, n), i)

    def test_pivot_4(self):
        nums = list(map(int, '5670124'))
        for i, n in enumerate(nums):
            with self.subTest(n=n, i=i):
                self.assertEqual(Solution().search(nums, n), i)


class TestFindSmallest(unittest.TestCase):
    """empty arrays are not expected"""

    def test_single_element(self):
        self.assertEqual(Solution().findSmallestIndex([8]), 0)

    def test_pivot_0(self):
        nums = list(map(int, '0124567'))
        self.assertEqual(Solution().findSmallestIndex(nums), 0)

    def test_pivot_1(self):
        nums = list(map(int, '1245670'))
        self.assertEqual(Solution().findSmallestIndex(nums), 6)

    def test_pivot_2(self):
        nums = list(map(int, '2456701'))
        self.assertEqual(Solution().findSmallestIndex(nums), 5)

    def test_pivot_3(self):
        nums = list(map(int, '4567012'))
        self.assertEqual(Solution().findSmallestIndex(nums), 4)

    def test_pivot_4(self):
        nums = list(map(int, '5670124'))
        self.assertEqual(Solution().findSmallestIndex(nums), 3)

    def test_pivot_5(self):
        nums = list(map(int, '6701245'))
        self.assertEqual(Solution().findSmallestIndex(nums), 2)

    def test_pivot_6(self):
        nums = list(map(int, '7012456'))
        self.assertEqual(Solution().findSmallestIndex(nums), 1)


if __name__ == "__main__":
    unittest.main()
