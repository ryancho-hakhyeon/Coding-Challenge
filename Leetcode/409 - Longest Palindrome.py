# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for i in Counter(s).values():
            ans += i // 2 * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans


obj = Solution()

s = "abccccdd"
print(obj.longestPalindrome(s))     # Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd",
# whose length is 7.

s = "a"
print(obj.longestPalindrome(s))     # Output: 1
# Explanation: The longest palindrome that can be built is "a",
# whose length is 1.