# Given an integer array nums,
# find three numbers whose product is maximum
# and return the maximum product.

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


obj = Solution()

nums = [1,2,3]
print(obj.maximumProduct(nums))     # Output: 6

nums = [1,2,3,4]
print(obj.maximumProduct(nums))     # Output: 24


nums = [-1,-2,-3]
print(obj.maximumProduct(nums))     # Output: -6
