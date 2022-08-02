# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # Other Solution
        # res, count = 0, 0
        #
        # for n in nums:
        #     if count == 0:
        #         res = n
        #     count += (1 if n == res else -1)
        # return res

        count = {}
        res, maxCount = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res


ob = Solution()

nums = [3,2,3]
print(ob.majorityElement(nums))     # Output: 3

nums = [2,2,1,1,1,2,2]
print(ob.majorityElement(nums))     # Output: 2
