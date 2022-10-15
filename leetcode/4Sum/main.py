from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        if len(nums) < 4 or sum([i for i in nums[:4]]) > target:
            return res

        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.twoSum(nums, target, j + 1, i, j, res)

        return res

    def twoSum(self, nums, target, start, i, j, res):
        lo = start
        hi = len(nums) - 1

        while lo < hi:
            if lo != start and nums[lo] == nums[lo - 1]:
                lo += 1
                continue

            quad_sum = nums[i] + nums[j] + nums[lo] + nums[hi]

            if quad_sum == target:
                res.append([nums[i], nums[j], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            elif quad_sum > target:
                hi -= 1
            else:
                lo += 1
