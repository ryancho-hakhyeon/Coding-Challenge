# A message containing letters from A-Z can be encoded into numbers using the mapping.
# To decode an encoded message, all the digits must be grouped
# then mapped back into letters using the reverse of the mapping above
# (there may be multiple ways). For example, "11106" can be mapped into:
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped
# into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
# The test cases are generated so that the answer fits in a 32-bit integer.

def numDecodings(s: str) -> int:
    # It needs more study how to work
    
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        res = dfs(i+1)

        if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
            res += dfs(i+2)
        dp[i] = res

        return res

    return dfs(0)


s = "12"
print(numDecodings(s))  # Output: 2
# "12" could be decoded as "AB" (1 2) or "L" (12).

s = "226"
print(numDecodings(s))  # Output: 3
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

s = "06"
print(numDecodings(s))  # Output: 0
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").