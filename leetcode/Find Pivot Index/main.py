from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total_sum - nums[i] - left_sum:
                return i
            left_sum += nums[i]
        return -1


cases = (
    ([1,7,3,6,5,6], 3),
    ([1,2,3], -1),
    ([2,1,-1], 0)
)
for nums, idx in cases:
    assert Solution().pivotIndex(nums) == idx
