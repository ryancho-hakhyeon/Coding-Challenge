# Given an array, rotate the array to the right by k steps, where k is non-negative.
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

        # Different way of solution 1
        # for i in range(k):
        #     nums.insert(i, nums.pop())

        # Different way of solution 2
        # nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]


ob = Solution()

nums = [1,2,3,4,5,6,7]
k = 3
print(ob.rotate(nums, k))   # Output: [5,6,7,1,2,3,4]
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2
print(ob.rotate(nums, k))   # Output: [3,99,-1,-100]
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]