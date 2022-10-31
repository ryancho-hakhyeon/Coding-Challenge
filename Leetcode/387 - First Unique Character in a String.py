# Given a string s, find the first non-repeating
# character in it and return its index.
# If it does not exist, return -1.
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = Counter(s)

        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i

        return -1



obj = Solution()

s = "leetcode"
print(obj.firstUniqChar(s))     # Output: 0

s = "loveleetcode"
print(obj.firstUniqChar(s))     # Output: 2

s = "aabb"
print(obj.firstUniqChar(s))     # Output: -1
