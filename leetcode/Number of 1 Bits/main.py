class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return sum(1 if n & (1 << i) else 0 for i in range(32))
