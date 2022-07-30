from typing import List


# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly.
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            res.append([])
            res[i].append(1)
            for j in range(1, i):
                res[i].append(res[i - 1][j - 1] + res[i - 1][j])

            if i != 0:
                res[i].append(1)

        return res


ob = Solution()

print(ob.generate(5))   # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print(ob.generate(1))   # Output: [[1]]