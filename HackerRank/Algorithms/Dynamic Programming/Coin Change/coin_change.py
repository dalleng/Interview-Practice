#!/bin/python3

import unittest


def make_change(coins, n):
    memo = [0 for i in range(n+1)]
    memo[0] = 1

    for i, coin in enumerate(coins):
        for j in range(coin, len(memo)):
            memo[j] += memo[j-coin]

    return memo[n]


class MakeChangeTest(unittest.TestCase):

    def test_sample1(self):
        self.assertEqual(make_change([1, 2, 3], 4), 4)

    def test_sample2(self):
        self.assertEqual(make_change([2, 5, 3, 6], 10), 5)

    def test_n_lower_than_coin_denomination(self):
        self.assertEqual(make_change([1, 10], 3), 1)

    def test_no_combination_available(self):
        self.assertEqual(make_change([8, 5], 11), 0)


if __name__ == '__main__':
    unittest.main()
