# Given two strings s and t,
# return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from
# the original string by deleting some (can be none) of the characters
# without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        idx = 0
        for i in range(len(t)):
            if idx <= len(s) - 1 and s[idx] == t[i]:
                idx += 1

        return idx == len(s)


obj = Solution()

s = "abc"
t = "ahbgdc"
print(obj.isSubsequence(s, t))  # Output: true

s = "axc"
t = "ahbgdc"
print(obj.isSubsequence(s, t))  # Output: false
