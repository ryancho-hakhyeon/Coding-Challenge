# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u',
# and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        str_list = [letter for letter in s]

        left, right = 0, len(s) - 1

        while left <= right:
            if str_list[left] not in vowels and str_list[right] in vowels:
                left += 1
            elif str_list[right] not in vowels and str_list[left] in vowels:
                right -= 1
            elif str_list[left] in vowels and str_list[right] in vowels:
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1

        return ''.join(str_list)


obj = Solution()

s = "hello"
print(obj.reverseVowels(s))     # Output: "holle"

s = "leetcode"
print(obj.reverseVowels(s))     # Output: "leotcede"