# Given an integer columnNumber,
# return its corresponding column title as it appears in an Excel sheet.
#
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        res = ''

        while columnNumber > 0:
            n = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            temp = letters[n]
            res = ''.join((temp, res))

        return res


ob = Solution()

columnNumber = 1
print(ob.convertToTitle(columnNumber))  # Output: "A"

columnNumber = 28
print(ob.convertToTitle(columnNumber))  # Output: "AB"

columnNumber = 701
print(ob.convertToTitle(columnNumber))  # Output: "ZY"

