from typing import List


# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into a space-separated sequence
# of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]


ob = Solution()
s = 'leetcode'
wordDict = ["leet", "code"]
print(ob.wordBreak(s, wordDict))    # Output: true
# Return true because "leetcode" can be segmented as "leet code".

s = 'applepenapple'
wordDict = ["apple", "pen"]
print(ob.wordBreak(s, wordDict))    # Output: true
# Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

s = 'catsandog'
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(ob.wordBreak(s, wordDict))    # Output: false
