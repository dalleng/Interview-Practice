"""
Given an array of integers, every element appears twice
except for one. Find that single one.
https://leetcode.com/problems/single-number/
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
