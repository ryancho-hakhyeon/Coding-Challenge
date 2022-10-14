# Write a function that takes an unsigned integer and returns
# the number of '1' bits it has (also known as the Hamming weight).
#
# Note:
# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, the input will be given as a signed integer type.
# It should not affect your implementation, as the integer's internal
# binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation.
# Therefore, in Example 3, the input represents the signed integer. -3.


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res



ob = Solution()

n = '00000000000000000000000000001011'
print(ob.hammingWeight(n))  # Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

n = '00000000000000000000000010000000'
print(ob.hammingWeight(n))  # Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

n = '11111111111111111111111111111101'
print(ob.hammingWeight(n))  # Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.