# You have a set of integers s, which originally contains
# all the numbers from 1 to n.
# Unfortunately, due to some error,
# one of the numbers in s got duplicated to another number in the set,
# which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status
# of this set after the error.
#
# Find the number that occurs twice and the number that is missing
# and return them in the form of an array.

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        originSum = sum([i for i in range(1, len(nums) + 1)])
        repetition = sum(nums) - sum(set(nums))
        missingNum = originSum - sum(set(nums))

        return [repetition, missingNum]


obj = Solution()

nums = [1,2,2,4]
print(obj.findErrorNums(nums))  # Output: [2,3]

nums = [1,1]
print(obj.findErrorNums(nums))  # Output: [1,2]
