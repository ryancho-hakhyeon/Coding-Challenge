# Given an integer array nums,
# return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        counts = 1
        pre_elem = nums[0]

        for i in range(len(nums)):
            if nums[i] != pre_elem:
                counts += 1
                pre_elem = nums[i]

            if counts == 3:
                return nums[i]

        return nums[0]


obj = Solution()

nums = [3,2,1]
print(obj.thirdMax(nums))   # Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

nums = [1,2]
print(obj.thirdMax(nums))   # Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist,
# so the maximum (2) is returned instead.

nums = [2,2,3,1]
print(obj.thirdMax(nums))   # Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2
# (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.