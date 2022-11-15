# We define a harmonious array as an array where
# the difference between its maximum value and
# its minimum value is exactly 1.
#
# Given an integer array nums, return the length of
# its longest harmonious subsequence among all its possible subsequences.
#
# A subsequence of array is a sequence that can be derived from
# the array by deleting some or no elements without
# changing the order of the remaining elements.

from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Hash Map Solution
        hash_map, res = {}, 0

        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        for key in hash_map:
            if key + 1 in hash_map:
                res = max(res, hash_map[key] + hash_map[key + 1])

        return res

        # Sorting Solution - very slow
        # nums.sort()
        # res = 0
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i - 1] == 1:
        #         tmp = nums.count(nums[i]) + nums.count(nums[i - 1])
        #         res = max(res, tmp)
        #
        # return res


obj = Solution()

nums = [1,3,2,2,5,2,3,7]
print(obj.findLHS(nums))    # Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

nums = [1,2,3,4]
print(obj.findLHS(nums))    # Output:2

nums = [1,1,1,1]
print(obj.findLHS(nums))    # Output: 0
