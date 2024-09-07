from typing import List

# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0

        # bring all non zero numbers to the start
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
        
        # fill the remaining positions with 0s
        for j in range(start, len(nums)):
            nums[j] = 0


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
assert nums == [1,3,12,0,0]

nums = [0]
Solution().moveZeroes(nums)
assert nums == [0]
