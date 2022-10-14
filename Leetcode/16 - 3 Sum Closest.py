# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])

        for i in range(len(nums) - 2):
            s = i + 1
            e = len(nums) - 1

            while s < e:
                sumoflist = nums[i] + nums[s] + nums[e]

                if abs(sumoflist - target) < abs(res - target):
                    res = sumoflist

                if sumoflist < target:
                    s += 1
                else:
                    e -= 1
        return res


ob = Solution()
nums = [-1,2,1,-4]
target = 1

print(ob.threeSumClosest(nums, target))     # Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

nums = [0,0,0]
target = 0

print(ob.threeSumClosest(nums, target))     # Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).