import unittest


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        mem = []
        max_profit = 0

        for i, price in enumerate(prices):
            profit = max(price - prices[i-1] + mem[i-1]
                         if i > 0 else 0, 0)
            mem.append(profit)

            if max_profit is None or profit > max_profit:
                max_profit = profit

        return max_profit


class MaxProfitTest(unittest.TestCase):
    def test_empty(self):
        self.assertEquals(Solution().maxProfit([]), 0)

    def test_single(self):
        self.assertEquals(Solution().maxProfit([300]), 0)

    def test_profit(self):
        l = [400, 100, 200, 110, 500, 125]
        self.assertEquals(Solution().maxProfit(l), 400)

    def test_no_profit(self):
        l = [100, 70]
        self.assertEquals(Solution().maxProfit(l), 0)


if __name__ == '__main__':
    unittest.main()
