# Given two strings s and t,
# return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1

        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1

        # for i in range(len(s)):
        #     if s[i] not in s_dict:
        #         s_dict[s[i]] = 1
        #     else:
        #         s_dict[s[i]] += 1
        #
        #     if t[i] not in t_dict:
        #         t_dict[t[i]] = 1
        #     else:
        #         t_dict[t[i]] += 1

        return s_dict == t_dict


obj = Solution()

s = "anagram"
t = "nagaram"
print(obj.isAnagram(s, t))  # Output: true

s = "rat"
t = "car"
print(obj.isAnagram(s, t))  # Output: false