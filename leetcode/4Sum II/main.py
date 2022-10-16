from typing import List


class Solution:
    def fourSumCountBruteForce(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        from itertools import product

        return sum([1 if sum(combination) == 0 else 0 for combination in product(nums1, nums2, nums3, nums4)])

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0
        memo = {}
        for num1 in nums1:
            for num2 in nums2:
                if num1 + num2 not in memo:
                    memo[num1 + num2] = 1
                else:
                    memo[num1 + num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                complement = -1 * (num3 + num4)
                result += memo.get(complement, 0)

        return result


lists = [[0, 1, -1], [-1, 1, 0], [0, 0, 1], [-1, 1, 1]]
assert Solution().fourSumCountBruteForce(*lists) == Solution().fourSumCount(*lists)
