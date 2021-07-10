from typing import List


class Solution:
    def twoSum(self, nums, target, start, res):
        hi = len(nums) - 1
        lo = start

        while lo < hi:
            if lo != start and nums[lo] == nums[lo - 1]:
                lo += 1
                continue

            if nums[lo] + nums[hi] == target:
                res.append([-target, nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                lo += 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.twoSum(nums, -n, i + 1, res)
        return res
