# You are given an integer array nums consisting of n elements,
# and an integer k.
#
# Find a contiguous subarray whose length is equal to k
# that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # maxSum = float('-inf')
        # for i in range(len(nums) - k + 1):
        #     fourSum = sum(nums[i:i + k])
        #     maxSum = max(fourSum, maxSum)
        #
        # return maxSum / k

        fourSum = sum(nums[:k])
        maxSum = fourSum
        for i in range(len(nums) - k):
            fourSum -= nums[i]
            fourSum += nums[i + k]
            maxSum = max(maxSum, fourSum)

        return maxSum / k


obj = Solution()

nums = [1,12,-5,-6,50,3]
k = 4
print(obj.findMaxAverage(nums, k))  # Output: 12.75000
# Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

nums = [5]
k = 1
print(obj.findMaxAverage(nums, k))  # Output: 5.00000