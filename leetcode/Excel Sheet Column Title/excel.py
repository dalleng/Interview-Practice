import unittest
from string import uppercase


class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        title = []
        quotient = n
        base = len(uppercase)

        while quotient > base:
            quotient, remainder = divmod(quotient, base)
            title.append(uppercase[remainder - 1])
            if remainder == 0:
                quotient -= 1

        title.append(uppercase[quotient - 1])
        return "".join(reversed(title))


class ConvertTest(unittest.TestCase):
    def test_tests(self):
        s = Solution()
        self.assertEquals(s.convertToTitle(26), "Z")
        self.assertEquals(s.convertToTitle(27), "AA")
        self.assertEquals(s.convertToTitle(52), "AZ")
        self.assertEquals(s.convertToTitle(468096), "ZPKR")


if __name__ == "__main__":
    unittest.main()
