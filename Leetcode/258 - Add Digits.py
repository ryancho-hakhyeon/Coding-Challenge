# Given an integer num, repeatedly add all its digits
# until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        # Using loop
        #         numStr = str(num)

        #         while len(numStr) > 1:
        #             res = 0
        #             for i in range(len(numStr)):
        #                 res += int(numStr[i])
        #             numStr = str(res)

        #         return int(numStr)

        # Without any loop
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9


obj = Solution()

num = 38
print(obj.addDigits(num))   # Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

num = 0
print(obj.addDigits(num))   # Output: 0
# reference: https://leetcode.com/problems/add-digits/solution/