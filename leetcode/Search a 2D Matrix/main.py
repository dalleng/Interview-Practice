import unittest


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix is None or not len(matrix):
            return False

        m = len(matrix)
        n = len(matrix[0])
        get_row = lambda i: i // n
        get_col = lambda i: i % n

        left = 0
        right = m * n - 1

        while right >= left:
            middle = (right - left) / 2 + left
            row = get_row(middle)
            col = get_col(middle)

            if target > matrix[row][col]:
                left = middle + 1
            elif target < matrix[row][col]:
                right = middle - 1
            else:
                return True

        return False


class SearchMatrixTest(unittest.TestCase):
    def test_none(self):
        m = None
        s = Solution()
        self.assertFalse(s.searchMatrix(m, 3))

    def test_empty(self):
        m = []
        s = Solution()
        self.assertFalse(s.searchMatrix(m, 3))

    def test_example(self):
        m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        s = Solution()
        self.assertTrue(s.searchMatrix(m, 3))

    def test_single_row(self):
        m = [[1, 2, 5, 6, 8, 10, 15]]
        s = Solution()

        for i in m[0]:
            self.assertTrue(s.searchMatrix(m, i))

        self.assertFalse(s.searchMatrix(m, 3))
        self.assertFalse(s.searchMatrix(m, 9))


if __name__ == "__main__":
    unittest.main()
