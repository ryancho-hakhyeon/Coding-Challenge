# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in s.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        word_pattern_dict = {}

        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in word_pattern_dict:
                word_pattern_dict[pattern[i]] = words[i]
            elif words[i] != word_pattern_dict[pattern[i]]:
                return False

        return True


obj = Solution()

pattern = "abba"
s = "dog cat cat dog"
print(obj.wordPattern(pattern, s))  # Output: true

pattern = "abba"
s = "dog cat cat fish"
print(obj.wordPattern(pattern, s))  # Output: false

pattern = "aaaa"
s = "dog cat cat dog"
print(obj.wordPattern(pattern, s))  # Output: false