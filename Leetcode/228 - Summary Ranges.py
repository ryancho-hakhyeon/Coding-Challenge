# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers
# in the array exactly. That is, each element of nums is covered by exactly
# one of the ranges,
# and there is no integer x such that x is in one of the rages but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []

        if n == 0:
            return res

        first_value = nums[0]

        for i in range(n):
            if i == n - 1 or nums[i] + 1 != nums[i + 1]:
                if nums[i] != first_value:
                    res.append(f"{first_value}->{nums[i]}")
                else:
                    res.append(f"{first_value}")

                if i != n - 1:
                    first_value = nums[i + 1]
        return res


obj = Solution()

nums = [0,1,2,4,5,7]
print(obj.summaryRanges(nums))  # Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

nums = [0,2,3,4,6,8,9]
print(obj.summaryRanges(nums))  # Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
