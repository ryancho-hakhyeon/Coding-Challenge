# The complement of an integer is the integer you get
# when you flip all the 0's to 1's
# and all the 1's to 0's in its binary representation.
# For example, The integer 5 is "101" in binary
# and its complement is "010" which is the integer 2.
# Given an integer num, return its complement.

class Solution:
    def findComplement(self, num: int) -> int:
        bin_str = str(bin(num)[2:])
        complement = []
        for s in bin_str:
            if s is '0':
                complement.append('1')
            else:
                complement.append('0')

        return int(''.join(complement), 2)


obj = Solution()

num = 5
print(obj.findComplement(num))  # Output: 2
# Explanation: The binary representation of 5 is 101
# (no leading zero bits), and its complement is 010. So you need to output 2.

num = 1
print(obj.findComplement(num))  # Output: 0
# Explanation: The binary representation of 1 is 1
# (no leading zero bits), and its complement is 0. So you need to output 0.