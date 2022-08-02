# Given a list of non-negative integers nums, arrange them
# such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
from typing import List
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key=functools.cmp_to_key(compare))

        return str(int("".join(nums)))


ob = Solution()

nums = [10, 2]
print(ob.largestNumber(nums))   # Output: "210"

nums = [3, 30, 34, 5, 9]
print(ob.largestNumber(nums))   # Output: "9534330"