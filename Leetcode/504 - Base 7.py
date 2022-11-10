# Given an integer num, return a string of its base 7 representation.

class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        p = 1

        if num == 0:
            return "0"

        if num < 0:
            p = -1
            num = abs(num)

        while num > 0:

            ans += str(num % 7)
            num //= 7

        ans = int(ans[::-1]) * p

        return str(ans)


obj = Solution()

num = 100
print(obj.convertToBase7(num))  # Output: "202"

num = -7
print(obj.convertToBase7(num))  # Output: "-10"
