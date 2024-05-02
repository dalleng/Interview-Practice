"""
1. Shopping Options

An Amazon customer wants to buy a pair of jeans, a pair of shoes, a skirt,
and a top but has a limited budget in dollars. Given different pricing options
for each product, determine how many options our customer has to buy 1
of each product. You cannot spend more money than the budgeted
amount.

Example
priceOfleans = [2, 3]
priceOfShoes = [4]
priceOfSkirts = [2, 3]
priceOfTops = [1, 2]
budgeted = 10

The customer must buy shoes for 4 dollars since there is only one option.
This leaves 6 dollars to spend on the other 3 items. Combinations of prices
paid for jeans, skirts, and tops respectively that add up to 6 dollars or less
are [2, 2, 2], [2, 2, 1], [3, 2, 1], [2, 3, 1]. There are 4 ways the customer can
purchase all 4 items.

Function Description

Complete the getNumberOfOptions function in the editor below. The
function must return an integer which represents the number of options
present to buy the four items.

getNumberOfOptions has 5 parameters:

int[] priceOfJeans: An integer array, which contains the prices of the pairs
of jeans available.
int[] priceOfShoes: An integer array, which contains the prices of the pairs
of shoes available.
int[] priceOfSkirts: An integer array, which contains the prices of the skirts
available.
int[] priceOfTops: An integer array, which contains the prices of the tops
available.
int dollars: the total number of dollars available to shop with.

Constraints

- 1 <= a, b, c, d <= 10^3
- 1 <= dollars <= 10^9
• 1 ≤ price of each item < 10^9

Note: a, b, c and d are the sizes of the four price arrays
"""
import unittest
from random import randint


# this problem can be turned into a version of 4sum
def getNumberOfOptionsBF(
    priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars
):
    priceOfJeans.sort()
    priceOfShoes.sort()
    priceOfSkirts.sort()
    priceOfTops.sort()
    solutions = 0

    for pj in priceOfJeans:
        max_pj = dollars - (priceOfShoes[0] + priceOfSkirts[0] + priceOfTops[0])
        if pj > max_pj:
            break

        for ps in priceOfShoes:
            max_ps = dollars - (pj + priceOfSkirts[0] + priceOfTops[0])
            if ps > max_ps:
                break

            for psk in priceOfSkirts:
                max_psk = dollars - (pj + ps + priceOfTops[0])
                if psk > max_psk:
                    break

                for pt in priceOfTops:
                    max_pt = dollars - (pj + ps + psk)
                    if pt > max_pt:
                        break
                    else:
                        solutions += 1
    return solutions


def getNumberOfOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    """
    The solutions for this problem was inspired in the 4-sum and it's different
    variations.
    """
    priceOfJeans.sort()
    priceOfShoes.sort()
    priceOfSkirts.sort()
    priceOfTops.sort()
    solutions = 0

    # print(f'dollars: {dollars}')
    # print(f'priceOfJeans: {priceOfJeans}')
    # print(f'priceOfShoes: {priceOfShoes}')
    # print(f'priceOfSkirts: {priceOfSkirts}')
    # print(f'priceOfTops: {priceOfTops}')

    for pj in priceOfJeans:
        max_pj = dollars - (priceOfShoes[0] + priceOfSkirts[0] + priceOfTops[0])
        # print(f'max_pj: {max_pj}')
        if pj > max_pj:
            break

        # print(f'pj: {pj}')

        for ps in priceOfShoes:
            max_ps = dollars - (pj + priceOfSkirts[0] + priceOfTops[0])
            # print(f'max_ps: {max_ps}')
            if ps > max_ps:
                break

            # print(f'ps: {ps}')

            j = None
            for psk in priceOfSkirts:
                max_psk = dollars - (pj + ps + priceOfTops[0])
                if psk > max_psk:
                    break

                # print(f'psk: {psk}')

                j = 0 if j is None else j
                while j < len(priceOfTops):
                    cost_so_far = pj + ps + psk
                    if cost_so_far + priceOfTops[j] > dollars:
                        while j > 0 and cost_so_far + priceOfTops[j] > dollars:
                            j -= 1
                        if cost_so_far + priceOfTops[j] <= dollars:
                            solutions += j + 1
                        break
                    else:
                        if j == len(priceOfTops) - 1:
                            solutions += j + 1
                            break
                        j += 1

    return solutions


class GetNumberOfOptionsTest(unittest.TestCase):
    @staticmethod
    def generate_list_of_prices():
        list_of_prices = []
        for i in range(4):
            items = randint(1, 100)
            list_of_prices.append([randint(1, 100) for _ in range(items)])

        return list_of_prices

    def test_example(self):
        self.assertEqual(getNumberOfOptions([2, 3], [4], [2, 3], [1, 2], 10), 4)

    def test_increase_j_to_max_then_decrease(self):
        solutions = getNumberOfOptions([1], [1], [1, 2, 10, 20, 30], [2, 3, 4], 14)
        self.assertEqual(solutions, 7)
        solutions = getNumberOfOptions([1], [1], [1, 2, 10, 20, 30], [2, 3, 4], 15)
        self.assertEqual(solutions, 8)

    def test_generate_cases(self):
        import time

        N_TESTS = 10
        for i in range(N_TESTS):
            list_of_prices = self.generate_list_of_prices()
            print("-" * 80)
            print(f"Test Case: {i}")
            dollars = randint(1, 1_000_000_000)
            start = time.time()
            brute_force_solution = getNumberOfOptionsBF(*list_of_prices, dollars)
            print("brute_force_solution took {}", time.time() - start)
            print("brute_force_solution", brute_force_solution)
            start = time.time()
            non_bf_solution = getNumberOfOptions(*list_of_prices, dollars)
            print("non_bf_solution", non_bf_solution)
            print("non_bf_solution took {}", time.time() - start)
            self.assertEqual(brute_force_solution, non_bf_solution)


if __name__ == "__main__":
    unittest.main()
