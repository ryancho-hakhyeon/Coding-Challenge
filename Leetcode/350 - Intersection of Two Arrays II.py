# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must appear as many times as
# it shows in both arrays and you may return the result in any order.
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        count_num = Counter(nums1)
        res = []
        for i in range(len(nums2)):
            if count_num[nums2[i]] > 0:
                res.append(nums2[i])
                count_num[nums2[i]] -= 1

        return res


obj = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
print(obj.intersect(nums1, nums2))   # Output: [2]

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(obj.intersect(nums1, nums2))   # Output: [9,4]
# Explanation: [4,9] is also accepted.