# Given an integer n, return an array ans of length n + 1 such that
# for each i (0 <= i <= n), ans[i] is the number of
# 1's in the binary representation of i.
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(bin(i).count('1'))

        return res


obj = Solution()

n = 2
print(obj.countBits(n))     # Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

n = 5
print(obj.countBits(n))     # Output: [0,1,1,2,1,2]
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
