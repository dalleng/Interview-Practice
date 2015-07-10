class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = (right - left) / 2 + left
            mid_squared = mid * mid
            if mid_squared == x:
                break
            elif mid_squared < x:
                if (mid + 1) * (mid + 1) > x:
                    break
                left = mid + 1
            elif mid_squared > x:
                right = mid - 1
        return mid
