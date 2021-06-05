from collections import OrderedDict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = OrderedDict()
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        for i, char in enumerate(s):
            if counter[char] == 1:
                return i

        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.firstUniqChar("leetcode") == 0
    assert solution.firstUniqChar("loveleetcode") == 2
    assert solution.firstUniqChar("aabb") == -1
