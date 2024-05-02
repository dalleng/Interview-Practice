import unittest


class Solution:
    # @param n, an integer
    # @return an integer

    def reverseBits(self, n):
        mask = 1
        reverse = 0

        for i in range(32):
            offset = 31 - 2 * i
            if offset > 0:
                reverse |= (n & (mask << i)) << offset
            else:
                reverse |= (n & (mask << i)) >> abs(offset)

        return reverse


class TestReverseBits(unittest.TestCase):
    s = Solution()

    def test_example(self):
        self.assertEquals(self.s.reverseBits(43261596), 964176192)


if __name__ == "__main__":
    unittest.main()
