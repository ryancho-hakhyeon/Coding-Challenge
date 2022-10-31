# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)

        for key, item in ransomNote_dict.items():
            if key not in magazine_dict or magazine_dict[key] < item:
                return False

        return True


obj = Solution()

ransomNote = "a"
magazine = "b"
print(obj.canConstruct(ransomNote, magazine))   # Output: false

ransomNote = "aa"
magazine = "ab"
print(obj.canConstruct(ransomNote, magazine))   # Output: false

ransomNote = "aa"
magazine = "aab"
print(obj.canConstruct(ransomNote, magazine))   # Output: true