import unittest
import heapq
from math import sqrt


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        d = self.distance(0, 0, x, y)
        seen = set()
        # print(f'd: {d}')
        frontier = []
        heapq.heappush(frontier, (d, 0, 0, 0))

        while frontier:
            d, steps, current_x, current_y = heapq.heappop(frontier)

            if (current_x, current_y) in seen:
                continue

            seen.add((current_x, current_y))
            print(f'steps: {steps} d: {d} current_x: {current_x} current_y: {current_y}')

            if (current_x, current_y) == (x, y):
                return steps

            for new_x, new_y in self.moves_for_position(current_x, current_y):
                new_d = self.distance(new_x, new_y, x, y)
                heapq.heappush(frontier, (new_d + steps, steps + 1, new_x, new_y))

    @staticmethod
    def distance(x1: int, y1: int, x2: int, y2: int) -> int:
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def moves_for_position(x: int, y: int) -> int:
        for d_x in (-1, 1):
            for d_y in (-2, 2):
                yield (x + d_x, y + d_y)

        for d_x in (-2, 2):
            for d_y in (-1, 1):
                yield (x + d_x, y + d_y)


class RemoveElementsTest(unittest.TestCase):
    s = Solution()

    def test_1(self):
        self.assertEqual(self.s.minKnightMoves(2, 112), 56)
        self.assertEqual(self.s.minKnightMoves(5, 5), 4)


if __name__ == '__main__':
    unittest.main()
