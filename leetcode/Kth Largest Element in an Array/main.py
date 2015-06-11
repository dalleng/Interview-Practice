"""
Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import unittest
import heapq


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        heap = []
        count = 0
        for i in nums:
            if count < k:
                heapq.heappush(heap, i)
                count += 1
            else:
                heapq.heappushpop(heap, i)
        return heap[0]


class FindKthLargestTest(unittest.TestCase):
    s = Solution()

    def test_example(self):
        l = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEquals(self.s.findKthLargest(l, k), 5)


if __name__ == '__main__':
    unittest.main()
