from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i, n in enumerate(nums):
            hi = len(nums) - 1
            lo = i + 1

            while lo < hi:
                if nums[lo] + nums[hi] + n < target:
                    count += hi - lo
                    lo += 1
                else:
                    hi -= 1

        return count
