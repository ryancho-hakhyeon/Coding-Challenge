# Given a binary array nums,
# return the maximum number of consecutive 1's in the array.
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        max_count = max(max_count, count)

        return max_count


obj = Solution()

nums = [1,1,0,1,1,1]
print(obj.findMaxConsecutiveOnes(nums))     # Output: 3
# Explanation: The first two digits or
# the last three digits are consecutive 1s.
# The maximum number of consecutive 1s is 3.

nums = [1,0,1,1,0,1]
print(obj.findMaxConsecutiveOnes(nums))     # Output: 2