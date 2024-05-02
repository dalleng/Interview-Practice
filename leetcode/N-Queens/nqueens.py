import unittest
from collections import Counter


class Solution:
    def check_position(self, board, row, col):
        if Counter(board[row])["Q"] > 1:
            return False

        cols = [r[col] for r in board]

        if Counter(cols)["Q"] > 1:
            return False

        diagonal_elements = Counter(board[row][col])
        diagonal_elements.update(
            board[r][c] for r, c in self.iter_diagonals(len(board), row, col)
        )

        if diagonal_elements["Q"] > 1:
            return False

        return True

    def iter_diagonals(self, n, row, col):
        for i in range(1, max(row + 1, n - row)):
            for row_offset, col_offset in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
                r, c = (row + (i * row_offset), col + (i * col_offset))
                if 0 <= r < n and 0 <= c < n:
                    yield r, c

    def filter_domains(self, domains, row, col):
        domains = [[r for r in domain if r != row] for domain in domains]
        for r, c in self.iter_diagonals(len(domains), row, col):
            domains[c] = [i for i in domains[c] if i != r]
        return domains

    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        board = ["." * n for _ in range(n)]
        domains = [range(n) for _ in range(n)]
        solutions = []

        def solve(col, domains):
            for row in domains[col]:
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]

                if self.check_position(board, row, col):
                    if col == n - 1:
                        solutions.append(board[:])
                    else:
                        filtered = self.filter_domains(domains, row, col)
                        solve(col + 1, filtered)

                board[row] = board[row][:col] + "." + board[row][col + 1 :]

        solve(0, domains)
        return solutions


class NQueensTest(unittest.TestCase):
    """
    Ran 3 tests in 1.305s
    """

    def test_4_queens(self):
        s = Solution()
        solutions = s.solveNQueens(4)
        expected = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
        self.assertEquals(set(map(str, solutions)), set(map(str, expected)))

    def test_8_queens(self):
        s = Solution()
        solutions = s.solveNQueens(8)
        self.assertEquals(len(solutions), 92)

    def test_9_queens(self):
        s = Solution()
        solutions = s.solveNQueens(9)
        self.assertEquals(len(solutions), 352)

    def test_10_queens(self):
        s = Solution()
        solutions = s.solveNQueens(10)
        self.assertEquals(len(solutions), 724)

    def test_11_queens(self):
        s = Solution()
        solutions = s.solveNQueens(11)
        self.assertEquals(len(solutions), 2680)

    def test_12_queens(self):
        s = Solution()
        solutions = s.solveNQueens(12)
        self.assertEquals(len(solutions), 14200)


if __name__ == "__main__":
    unittest.main()
