# The Fibonacci numbers, commonly denoted F(n) form a sequence,
# called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones,
# starting from 0 and 1.
# That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        return self.fib(n-1) + self.fib(n-2)


obj = Solution()

n = 2
print(obj.fib(n))   # Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

n = 3
print(obj.fib(n))   # Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

n = 4
print(obj.fib(n))   # Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.