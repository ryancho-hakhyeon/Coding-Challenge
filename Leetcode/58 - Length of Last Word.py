# Given a string s consisting of words and spaces,
# return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pass


ob = Solution()

s = "Hello World"
print(ob.lengthOfLastWord(s))   # Output: 5
# Explanation: The last word is "World" with length 5.

s = "   fly me   to   the moon  "
print(ob.lengthOfLastWord(s))   # Output: 4
# Explanation: The last word is "moon" with length 4.

s = "luffy is still joyboy"
print(ob.lengthOfLastWord(s))   # Output: 6
# Explanation: The last word is "joyboy" with length 6.