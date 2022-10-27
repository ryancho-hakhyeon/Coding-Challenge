# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must be unique
# and you may return the result in any order.
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        newNums1 = set(nums1)
        newNums2 = set(nums2)

        if len(newNums1) < len(newNums2):
            return [n for n in newNums2 if n in newNums1]
        else:
            return [n for n in newNums1 if n in newNums2]


obj = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
print(obj.intersection(nums1, nums2))   # Output: [2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(obj.intersection(nums1, nums2))   # Output: [9,4]
# Explanation: [4,9] is also accepted.
