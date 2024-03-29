# You have a long flowerbed in which some of
# the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return if n new flowers can be planted in the flowerbed
# without violating the no-adjacent-flowers rule.
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1

        return count >= n

        # or

        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 0:
        #         empty_left = (i == 0) or (flowerbed[i - 1] == 0)
        #         empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
        #
        #         if empty_left and empty_right:
        #             flowerbed[i] = 1
        #             n -= 1
        #
        # return n <= 0


obj = Solution()

flowerbed = [1,0,0,0,1]
n = 1
print(obj.canPlaceFlowers(flowerbed, n))    # Output: true

flowerbed = [1,0,0,0,1]
n = 2
print(obj.canPlaceFlowers(flowerbed, n))    # Output: false
