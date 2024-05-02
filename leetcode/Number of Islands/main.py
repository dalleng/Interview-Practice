from typing import List


WATER, LAND = ("0", "1")


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_islands = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND and (i, j) not in seen:
                    self.traversal((i, j), grid, seen)
                    n_islands += 1
        return n_islands

    def traversal(self, start, grid, seen):
        frontier = [start]
        while frontier:
            i, j = frontier.pop()
            seen.add((i, j))

            if i - 1 >= 0 and grid[i - 1][j] == LAND and (i - 1, j) not in seen:
                frontier.append((i - 1, j))

            if i + 1 < len(grid) and grid[i + 1][j] == LAND and (i + 1, j) not in seen:
                frontier.append((i + 1, j))

            if j - 1 >= 0 and grid[i][j - 1] == LAND and (i, j - 1) not in seen:
                frontier.append((i, j - 1))

            if (
                j + 1 < len(grid[0])
                and grid[i][j + 1] == LAND
                and (i, j + 1) not in seen
            ):
                frontier.append((i, j + 1))


if __name__ == "__main__":
    s = Solution()
    assert s.numIslands(["0"]) == 0
    assert s.numIslands(["1"]) == 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert s.numIslands(grid) == 3
