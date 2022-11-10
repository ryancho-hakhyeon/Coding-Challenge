# Given an array of strings words,
# return the words that can be typed using letters of the alphabet
# on only one row of American keyboard like the image below.
#
# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = {'q','w','e','r','t','y','u','i','o','p'}
        set2 = {'a','s','d','f','g','h','j','k','l'}
        set3 = {'z','x','c','v','b','n','m'}

        res = []

        for word in words:
            word_set = set(word.lower())
            if (word_set&set1 == word_set) or (word_set&set2 == word_set) or (word_set&set3 == word_set):
                res.append(word)

        return res


obj = Solution()

words = ["Hello","Alaska","Dad","Peace"]
print(obj.findWords(words))     # Output: ["Alaska","Dad"]

words = ["omk"]
print(obj.findWords(words))     # Output: []

words = ["adsdf","sfd"]
print(obj.findWords(words))     # Output: ["adsdf","sfd"]