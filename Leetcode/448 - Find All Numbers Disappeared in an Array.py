# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n]
# that do not appear in nums.
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -1 * abs(nums[index])

        res = []

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res


obj = Solution()

nums = [4,3,2,7,8,2,3,1]
print(obj.findDisappearedNumbers(nums))     # Output: [5,6]

nums = [1,1]
print(obj.findDisappearedNumbers(nums))     # Output: [2]
