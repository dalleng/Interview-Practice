from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if (mid == 0 or nums[mid] < nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[hi] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
