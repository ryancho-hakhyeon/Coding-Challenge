# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def helper(num, factor):
            while num % factor == 0:
                num //= factor
            return num

        for i in [2, 3, 5]:
            n = helper(n, i)

        return n == 1


obj = Solution()

n = 6
print(obj.isUgly(n))    # Output: true
# Explanation: 6 = 2 × 3

n = 1
print(obj.isUgly(n))    # Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

n = 14
print(obj.isUgly(n))    # Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.