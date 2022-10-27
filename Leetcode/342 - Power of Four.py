# Given an integer n, return true if it is a power of four.
# Otherwise, return false.
#
# An integer n is a power of four,
# if there exists an integer x such that n == 4x.
from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n < 1:
        #     return False
        #
        # while n % 4 == 0:
        #     n /= 4
        #
        # return n == 1
        if n <= 0:
            return False
        res = log(n) / log(4)
        return res.is_integer()


obj = Solution()

n = 16
print(obj.isPowerOfFour(n))     # Output: true

n = 5
print(obj.isPowerOfFour(n))     # Output: false

n = 1
print(obj.isPowerOfFour(n))     # Output: true