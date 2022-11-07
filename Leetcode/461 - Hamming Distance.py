# The Hamming distance between two integers is
# the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0

        for _ in range(32):
            count += xor & 1
            xor = xor >> 1

        return count


obj = Solution()

x = 1
y = 4
print(obj.hammingDistance(x, y))    # Output: 2
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

x = 3
y = 1
print(obj.hammingDistance(x, y))    # Output: 1