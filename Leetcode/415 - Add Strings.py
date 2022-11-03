# Given two non-negative integers,
# num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
#
# You must solve the problem without using any built-in library
# for handling large integers (such as BigInteger).
# You must also not convert the inputs to integers directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        carry, i, j = 0, len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1

            ans.append(str(carry % 10))
            carry = carry // 10

        return "".join(ans)[::-1]


obj = Solution()

num1 = "11"
num2 = "123"
print(obj.addStrings(num1, num2))   # Output: "134"

num1 = "456"
num2 = "77"
print(obj.addStrings(num1, num2))   # Output: "533"

num1 = "0"
num2 = "0"
print(obj.addStrings(num1, num2))   # Output: "0"