# Given an integer n, return true if it is a power of three.
# Otherwise, return false.
#
# An integer n is a power of three,
# if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n /= 3
        return n == 1


obj = Solution()

n = 27
print(obj.isPowerOfThree(n))    # Output: true
# Explanation: 27 = 33

n = 0
print(obj.isPowerOfThree(n))    # Output: false
# Explanation: There is no x where 3x = 0.

n = -1
print(obj.isPowerOfThree(n))    # Output: false
# Explanation: There is no x where 3x = (-1).