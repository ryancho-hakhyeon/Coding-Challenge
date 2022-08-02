# Given a string columnTitle that represents the column title
# as appears in an Excel sheet, return its corresponding column number.
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
    def titleToNumber(self, columnTitle: str) -> int:
        multiplier = 1
        res = 0

        for i in range(len(columnTitle) - 1, -1, -1):
            res += (ord(columnTitle[i]) - 64) * multiplier
            multiplier *= 26

        return res


ob = Solution()

columnTitle = "A"
print(ob.titleToNumber(columnTitle))    # Output: 1

columnTitle = "AB"
print(ob.titleToNumber(columnTitle))    # Output: 28

columnTitle = "ZY"
print(ob.titleToNumber(columnTitle))    # Output: 701


