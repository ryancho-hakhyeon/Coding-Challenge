# Given a string s, check if it can be constructed by taking
# a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        s_str = (s + s)[1:-1]

        return s in s_str


obj = Solution()

s = "abab"
print(obj.repeatedSubstringPattern(s))  # Output: true
# Explanation: It is the substring "ab" twice.

s = "aba"
print(obj.repeatedSubstringPattern(s))  # Output: false

s = "abcabcabcabc"
print(obj.repeatedSubstringPattern(s))  # Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.