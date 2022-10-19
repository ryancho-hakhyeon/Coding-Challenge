# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character
# while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in mapS and mapS[c1] != c2) or (c2 in mapT and mapT[c2] != c1):
                return False
            mapS[c1] = c2
            mapT[c2] = c1
        return True


ob = Solution()

s = "egg"
t = "add"
print(ob.isIsomorphic(s, t))    # Output: true

s = "foo"
t = "bar"
print(ob.isIsomorphic(s, t))    # Output: false

s = "paper"
t = "title"
print(ob.isIsomorphic(s, t))    # Output: true