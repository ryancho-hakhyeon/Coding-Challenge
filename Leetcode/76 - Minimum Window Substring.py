# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that every character
# in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.

def minWindow(s: str, t: str) -> str:
    # it is able to other way of getting result
    # let's try using for-loop inside of while-loop next time
    # also, you can use dict.pop(c) instead of adding have value
    if t == "":
        return ""

    count, window = {}, {}

    for c in t:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1

    l, have = 0, 0
    res, resLen = '', float('infinity')

    for i in range(len(s)):
        c = s[i]
        if c not in window:
            window[c] = 1
        else:
            window[c] += 1

        if c in t and window[c] == count[c]:
            have += 1

        while have == len(count):
            if (i - l + 1) < resLen:
                res = s[l:i+1]
                resLen = len(res)

            window[s[l]] -= 1

            if s[l] in count and window[s[l]] < count[s[l]]:
                have -= 1
            l += 1

    return res if resLen != float('infinity') else ""


s = 'ADOBECODEBANC'
t = 'ABC'
print(minWindow(s, t))  # Output: "BANC"
# The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

s = 'a'
t = 'a'
print(minWindow(s, t))  # Output: "a"
# The entire string s is the minimum window.

s = 'a'
t = 'aa'
print(minWindow(s, t))  # Output: ""
# Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.