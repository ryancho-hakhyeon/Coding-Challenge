# You are playing the following Nim Game with your friend:
# Initially, there is a heap of stones on the table.
# You and your friend will alternate taking turns, and you go first.
# On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
# The one who removes the last stone is the winner.
# Given n, the number of stones in the heap, return true
# if you can win the game assuming both you and your friend play optimally, otherwise return false.

class Solution:
    def canWinNim(self, n: int) -> bool:
        # One line, 4n
        # return (n % 4 != 0)

        # DP Solution
        if n > 100000000:
            return n % 4 != 0

        dp = [False] * (n + 1)

        def helper(n):
            if dp[n] or n in [1, 2, 3]:
                return True
            if n == 4:
                return False

            dp[n] = not (helper(n-1) and helper(n-2) and helper(n-3))

            return dp[n]

        return helper(n)


obj = Solution()

n = 4
print(obj.canWinNim(n))     # Output: false
# Explanation: These are the possible outcomes:
# 1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
# 2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
# 3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
# In all outcomes, your friend wins.

n = 1
print(obj.canWinNim(n))     # Output: true

n = 2
print(obj.canWinNim(n))     # Output: true
