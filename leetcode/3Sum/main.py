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
            # if the list is sorted and n > 0, only larger numbers will be
            # found ahead so there's no chance to find a pair of numbers that'd
            # sum to -n
            if n > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            self.twoSum(nums, -n, i + 1, res)
        return res


# Solution to the 3Sum problem that does not require sorting
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        solutions_seen = set()
        for i, n in enumerate(nums[:-2]):
            opposite = n * -1
            for solution in self.twoSum(nums, opposite, i + 1):
                if solution:
                    solution.append(n)
                    solution.sort()
                    if str(solution) not in solutions_seen:
                        solutions.append(solution)
                        solutions_seen.add(str(solution))
        return solutions

    def twoSum(self, nums: List[int], target: int, lo: int) -> List[List[int]]:
        seen = set()
        for n in nums[lo:]:
            if target - n in seen:
                yield [n, target - n]
            seen.add(n)
