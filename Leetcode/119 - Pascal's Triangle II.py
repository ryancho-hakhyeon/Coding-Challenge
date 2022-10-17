# Given an integer rowIndex,
# return the rowIndexth (0-indexed) row of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of
# the two numbers directly above it
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        res = []

        for i in range(rowIndex + 1):
            res.append([])
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i - 1][j - 1] + res[i - 1][j])

            if i != 0:
                res[i].append(1)

        return res[rowIndex]


ob = Solution()

rowIndex = 3
print(ob.getRow(rowIndex))  # Output: [1,3,3,1]

rowIndex = 0
print(ob.getRow(rowIndex))  # Output: [1]

rowIndex = 1
print(ob.getRow(rowIndex))  # Output: [1,1]