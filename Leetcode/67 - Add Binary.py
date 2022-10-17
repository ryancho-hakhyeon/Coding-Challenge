# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = ''
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while i >= 0 or j >= 0:
            sum_int = carry
            if i >= 0:
                sum_int += ord(a[i]) - ord('0')
            if j >= 0:
                sum_int += ord(b[j]) - ord('0')
            i -= 1
            j -= 1
            if sum_int > 1:
                carry = 1
            else:
                carry = 0
            res += str(sum_int % 2)

        if carry != 0:
            res += str(carry)

        return res[::-1]


ob = Solution()

a = "11"
b = "1"
print(ob.addBinary(a, b))   # Output: "100"

a = "1010"
b = "1011"
print(ob.addBinary(a, b))   # Output: "10101"