from collections import Counter

# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        same_chars = set(word1) == set(word2)
        same_counts = sorted(list(c1.values())) == sorted(list(c2.values()))
        return same_chars and same_counts


s = Solution()
assert s.closeStrings('abc', 'bca') == True
assert s.closeStrings('a', 'aa') == False
assert s.closeStrings('abbccc', 'cabbba') == True
assert s.closeStrings("uau", "ssx") == False
