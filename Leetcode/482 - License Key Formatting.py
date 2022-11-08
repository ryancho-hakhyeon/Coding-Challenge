# You are given a license key represented as a string s that
# consists of only alphanumeric characters and dashes.
# The string is separated into n + 1 groups by n dashes.
# You are also given an integer k.
#
# We want to reformat the string s such that each group contains
# exactly k characters, except for the first group,
# which could be shorter than k
# but still must contain at least one character.
# Furthermore, there must be a dash inserted between two groups,
# and you should convert all lowercase letters to uppercase.
#
# Return the reformatted license key.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        reversed_str = s.replace('-', '')[::-1]
        ans = []
        sub = ''
        for i in range(len(reversed_str)):
            sub += reversed_str[i].upper()
            if (i + 1) % k == 0:
                ans.append(sub)
                sub = ''

            if i + 1 == len(reversed_str) and sub:
                ans.append(sub)

        return "-".join(ans)[::-1]


obj = Solution()

s = "5F3Z-2e-9-w"
k = 4
print(obj.licenseKeyFormatting(s, k))   # Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts,
# each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.

s = "2-5g-3-J"
k = 2
print(obj.licenseKeyFormatting(s, k))   # Output: "2-5G-3J"
