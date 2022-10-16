import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = None
        i, j = 0, 0
        seen = {}

        while j < len(s):
            char = s[j]

            if char not in seen or seen[char] < i:
                seen[char] = j
                j += 1
            else:
                result = max(j - i, result or 0)
                seen_at = seen.pop(char)
                i = seen_at + 1

        return max(j - i, result or 0)


class RemoveElementsTest(unittest.TestCase):
    s = Solution()

    def test_1(self):
        string = "abcabcbb"
        self.assertEqual(self.s.lengthOfLongestSubstring(string), 3)

    def test_2(self):
        string = "aab"
        self.assertEqual(self.s.lengthOfLongestSubstring(string), 2)

    def test_3(self):
        string = "abba"
        self.assertEqual(self.s.lengthOfLongestSubstring(string), 2)


if __name__ == '__main__':
    unittest.main()
