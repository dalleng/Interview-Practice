# https://www.hackerrank.com/challenges/stockmax/problem
def stockmax(prices):
    profit = 0
    max_price = prices[-1]
    for price in reversed(prices):
        max_price = max(max_price, price)
        profit += max_price - price
    return profit


if __name__ == "__main__":
    assert stockmax([2, 1]) == 0
    assert stockmax([5, 3, 2]) == 0
    assert stockmax([1, 2, 100]) == 197
    assert stockmax([1, 3, 1, 2]) == 3
