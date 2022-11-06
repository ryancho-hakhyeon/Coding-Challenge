# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of
# the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        completeRows, i = 0, 1
        # Bruteforce Search
        # while n >= 0:
        #     n -= i
        #     if n >= 0:
        #         completeRows += 1
        #     i += 1
        # return completeRows

        start = 1
        end = n

        while start <= end:
            mid = start + (end - start) // 2

            if (mid * (mid + 1)) // 2 <= n:
                completeRows = mid
                start = mid + 1
            else:
                end = mid - 1

        return completeRows


obj = Solution()

n = 5
print(obj.arrangeCoins(n))  # Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.

n = 8
print(obj.arrangeCoins(n))  # Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.