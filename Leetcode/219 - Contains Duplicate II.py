# Given an integer array nums and an integer k, return true
# if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(i - dic[nums[i]]) <= k:
                    return True
                else:
                    dic[nums[i]] = i
            else:
                dic[nums[i]] = i

        return False


ob = Solution()

nums = [1,2,3,1]
k = 3
print(ob.containsNearbyDuplicate(nums, k))  # Output: true

nums = [1,0,1,1]
k = 1
print(ob.containsNearbyDuplicate(nums, k))  # Output: true

nums = [1,2,3,1,2,3]
k = 2
print(ob.containsNearbyDuplicate(nums, k))  # Output: false