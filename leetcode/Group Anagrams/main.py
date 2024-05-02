from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            grouped[key].append(str)
        return list(grouped.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
    print(
        s.groupAnagrams(
            ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
        )
    )
