import unittest
from string import uppercase


class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        if not s:
            return 0
        else:
            return sum(
                (uppercase.index(letter) + 1) * 26**i
                for i, letter in enumerate(reversed(s))
            )


class TitleToNumberTest(unittest.TestCase):
    def test_single_letter(self):
        s = Solution()
        for i in uppercase:
            self.assertEquals(s.titleToNumber(i), uppercase.index(i) + 1)

    def test_two_letters(self):
        s = Solution()
        self.assertEquals(s.titleToNumber("AA"), 27)
        self.assertEquals(s.titleToNumber("AB"), 28)


if __name__ == "__main__":
    unittest.main()
