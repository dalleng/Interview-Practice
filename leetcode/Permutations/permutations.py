class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        permutations = []

        def _permute(permutation):
            for i in nums:
                if i not in permutation:
                    _permute(permutation + [i])

            if (len(permutation) == len(nums) and
                    permutation not in permutations):
                permutations.append(permutation)

        _permute([])
        return permutations

print Solution().permute(range(1, 4))
