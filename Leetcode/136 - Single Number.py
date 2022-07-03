from typing import List


# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # memo = {}
        #
        # for n in nums:
        #     if n in memo:
        #         memo[n] += 1
        #     else:
        #         memo[n] = 1
        #
        # for key, value in memo.items():
        #     if value == 1:
        #         return key
        res = 0

        for n in nums:
            res = n ^ res
        return res

ob = Solution()

nums = [2, 2, 1]
print(ob.singleNumber(nums))    # Output: 1

nums = [4, 1, 2, 1, 2]
print(ob.singleNumber(nums))    # Output: 4

nums = [1]
print(ob.singleNumber(nums))    # Output: 1