
# There is a robot on an m x n grid. The robot is initially located
# at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109

def uniquePaths(m: int, n: int) -> int:
    # It happens the time limit exceeded
    # when the number is m = 23, n = 12
    def dp(row, col):
        if row < 0 or row > m-1 or col < 0 or col > n-1:
            return 0
        if row == m-1 and col == n-1:
            return 1

        count = 0
        count = dp(row+1, col) + dp(row, col+1)

        return count

    return dp(0, 0)

# print(uniquePaths(3, 7))    # Output: 28
# print(uniquePaths(3, 2))    # Output: 3


def uniquePaths_diff(m: int, n: int) -> int:
    # This solution is passed for all situations.

    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        dp[m-1][i] = 1

    for i in range(m-2, -1, -1):
        for j in range(n-1, -1, -1):
            if j+1 < n:
                dp[i][j] = dp[i][j] + dp[i+1][j]
                dp[i][j] = dp[i][j] + dp[i][j+1]
            else:
                dp[i][j] = dp[i][j] + dp[i + 1][j]
    return dp[0][0]


print(uniquePaths_diff(3, 7))   # Output: 28
print(uniquePaths_diff(3, 2))    # Output: 3
