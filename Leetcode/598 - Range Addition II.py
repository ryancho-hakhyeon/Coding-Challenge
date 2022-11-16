# You are given an m x n matrix M initialized with all 0's
# and an array of operations ops, where ops[i] = [ai, bi] means
# M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
#
# Count and return the number of maximum integers in the matrix
# after performing all the operations.
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # matrix = [[0 for _ in range(n)] for _ in range(m)]

        if not ops:
            return m * n
        min_row, min_col = float('inf'), float('inf')
        for op in ops:
            min_row = min(min_row, op[0])
            min_col = min(min_col, op[1])

        return min_row * min_col


obj = Solution()

m = 3
n = 3
ops = [[2,2],[3,3]]
print(obj.maxCount(m, n, ops))  # Output: 4
# Explanation: The maximum integer in M is 2,
# and there are four of it in M. So return 4.

m = 3
n = 3
ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
print(obj.maxCount(m, n, ops))  # Output: 4

m = 3
n = 3
ops = []
print(obj.maxCount(m, n, ops))  # Output: 9