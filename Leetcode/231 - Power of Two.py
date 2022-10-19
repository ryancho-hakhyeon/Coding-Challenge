# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        return n == 1 or (n % 2 == 0 and self.isPowerOfTwo(n // 2))



obj = Solution()

n = 1
print(obj.isPowerOfTwo(n))  # Output: true
# Explanation: 2**0 = 1

n = 16
print(obj.isPowerOfTwo(n))  # Output: true
# Explanation: 2**4 = 16

n = 3
print(obj.isPowerOfTwo(n))  # Output: false

