class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        mem = []
        max_sum = None
        for i in range(len(nums)):
            current_sum = max(0, mem[i - 1] if i > 0 else 0) + nums[i]
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
            mem.append(current_sum)
        return max_sum


assert Solution().maxSubArray([-1, 0, -2]) == 0
assert Solution().maxSubArray([-1, 5, 100, -1000]) == 105
assert Solution().maxSubArray([4, -1, 2, 1]) == 6
