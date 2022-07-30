from typing import List


# Given a string s, partition s such that every substring of
# the partition is a palindrome. Return all possible palindrome partitioning of s.
# A palindrome string is a string that reads the same backward as forward.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res


ob = Solution()
s = "aab"
print(ob.partition(s))  # Output: [["a","a","b"],["aa","b"]]

s = "a"
print(ob.partition(s))  # Output: [["a"]]