# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element,
# and return its index. If the array contains multiple peaks,
# return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words,
# an element is always considered to be strictly greater than
# a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Using binary search algorithm
        l, r = 0, len(nums)-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l


ob = Solution()

nums = [1,2,3,1]
print(ob.findPeakElement(nums))     # Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

nums = [1,2,1,3,5,6,4]
print(ob.findPeakElement(nums))     # Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.