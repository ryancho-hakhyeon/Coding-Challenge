# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # kind of hash map, but slower than second solution
        for i in range(max(nums)+1):
            if i not in nums:
                return i
        return len(nums)
        # set difference, faster than first solution
        # for n in set(range(len(nums) + 1)) - set(nums):
        #     return n


obj = Solution()

nums = [3, 0, 1]
print(obj.missingNumber(nums))  # Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3].
# 2 is the missing number in the range since it does not appear in nums.

nums = [0, 1]
print(obj.missingNumber(nums))  # Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2].
# 2 is the missing number in the range since it does not appear in nums.

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(obj.missingNumber(nums))  # Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9].
# 8 is the missing number in the range since it does not appear in nums.