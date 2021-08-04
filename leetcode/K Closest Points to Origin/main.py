import heapq
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        O(N*log(N)) Solution
        """
        q = []
        for x, y in points:
            heapq.heappush(q, (math.sqrt(x**2+y**2), x, y))
        closest = [[x, y] for _, x, y in heapq.nsmallest(k, q)]
        return closest

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        O(N*log(K)) Solution
        """
        q = []

        for x, y in points:
            if len(q) < k:
                heapq.heappush(q, (-math.sqrt(x**2+y**2), x, y))
            else:
                distance = math.sqrt(x**2+y**2)
                max_min_distance, _, _ = q[0]
                if -max_min_distance > distance:
                    heapq.heappushpop(q, (-distance, x, y))

        return [[x, y] for _, x, y in q]
