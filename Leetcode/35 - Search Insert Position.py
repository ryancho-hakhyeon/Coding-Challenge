# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start


ob = Solution()

nums = [1,3,5,6]
target = 5
print(ob.searchInsert(nums, target))    # Output: 2

nums = [1,3,5,6]
target = 2
print(ob.searchInsert(nums, target))    # Output: 1

nums = [1,3,5,6]
target = 7
print(ob.searchInsert(nums, target))    # Output: 4

