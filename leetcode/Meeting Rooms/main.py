import unittest
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        result = True
        for i in range(len(intervals) - 1):
            current = intervals[i]
            next = intervals[i + 1]
            if next[0] < current[1]:
                result = False
                break

        return result


class SolutionTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(Solution().canAttendMeetings([[13, 15], [1, 13]]), True)


if __name__ == "__main__":
    unittest.main()
