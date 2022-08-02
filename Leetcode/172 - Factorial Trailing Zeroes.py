# Given an integer n, return the number of trailing zeroes in n!.
# Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n // 5
            res += n

        return res

ob = Solution()

n = 3
print(ob.trailingZeroes(n))     # Output: 0
# Explanation: 3! = 6, no trailing zero.

n = 5
print(ob.trailingZeroes(n))     # Output: 1
# Explanation: 5! = 120, one trailing zero.

n = 7
print(ob.trailingZeroes(n))     # Output: 0
