# Given an integer array nums, find a contiguous non-empty subarray
# within the array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(temp, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)

        return res
    # This is other solution in the leetcode discuss.
    # def maxProduct(nums):
    #     dp = [[0 for i in range(2)] for i in range(len(nums))]
    #     print(dp)
    #
    #     dp[-1][0] = nums[-1]
    #     dp[-1][1] = nums[-1]
    #
    #     print(dp)
    #     for i in range(len(nums) - 2, -1, -1):
    #         dp[i][0] = max(nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1])
    #         dp[i][1] = min(nums[i], nums[i] * dp[i + 1][0], nums[i] * dp[i + 1][1])
    #     print(dp)
    #     maxi = float('-inf')
    #     for i in range(len(dp)):
    #         maxi = max(dp[i][0], dp[i][1], maxi)
    #     return maxi

ob = Solution()

nums = [2,3,-2,4]
print(ob.maxProduct(nums))  # Output: 6
# Explanation: [2,3] has the largest product 6.

nums = [-2,0,-1]
print(ob.maxProduct(nums))  # Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.