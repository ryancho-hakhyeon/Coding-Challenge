# Given a string s, reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split(" ")
        res = []

        for i in range(len(split_str)):
            res.append(split_str[i][::-1])

        return " ".join(res)


obj = Solution()

s = "Let's take LeetCode contest"
print(obj.reverseWords(s))  # Output: "s'teL ekat edoCteeL tsetnoc"

s = "God Ding"
print(obj.reverseWords(s))  # Output: "doG gniD"
