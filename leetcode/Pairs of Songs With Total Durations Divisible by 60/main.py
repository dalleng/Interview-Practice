from typing import List
import math
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        solutions = 0
        memo = Counter(time)
        largest = max(time)

        for t in time:
            multiples = (t + largest) // 60
            initial = math.ceil(t / 60)
            for m in range(initial, multiples + 1):
                target = (60 * m) - t
                if target in memo and memo[target]:
                    solutions += memo[t] * (memo[t] - 1) // 2 if target == t else memo[t] * memo[target]

            # avoid duplicate counts
            memo[t] = 0

        return solutions
