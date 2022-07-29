# Given an integer array nums, find a contiguous non-empty subarray
# within the array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pass


ob = Solution()

nums = [2,3,-2,4]
print(ob.maxProduct(nums))  # Output: 6
# Explanation: [2,3] has the largest product 6.

nums = [-2,0,-1]
print(ob.maxProduct(nums))  # Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.