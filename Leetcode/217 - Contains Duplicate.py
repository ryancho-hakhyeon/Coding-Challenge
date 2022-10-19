# Given an integer array nums, return true if any value appears at least twice
# in the array, and return false if every element is distinct.
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


ob = Solution()

nums = [1,2,3,1]
print(ob.containsDuplicate(nums))   # Output: true

nums = [1,2,3,4]
print(ob.containsDuplicate(nums))   # Output: false

nums = [1,1,1,3,3,4,3,2,4,2]
print(ob.containsDuplicate(nums))   # Output: true