# A perfect number is a positive integer
# that is equal to the sum of its positive divisors,
# excluding the number itself. A divisor of an integer x is an integer
# that can divide x evenly.
#
# Given an integer n, return true if n is a perfect number, otherwise return false.
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        ans = 0

        for n in range(1, math.floor(num**0.5) + 1):
            if num % n == 0:
                ans += n + num // n

        return ans == 2 * num


obj = Solution()

num = 28
print(obj.checkPerfectNumber(num))  # Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.

num = 7
print(obj.checkPerfectNumber(num))  # Output: false