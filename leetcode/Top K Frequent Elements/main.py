import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for n, count in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, n))
            else:
                if heap[0][0] < count:
                    heapq.heappushpop(heap, (count, n))

        return [n for _, n in heap]
