# Alice has n candies, where the ith candy is of type candyType[i].
# Alice noticed that she started to gain weight, so she visited a doctor.
#
# The doctor advised Alice to only eat n / 2 of the candies
# she has (n is always even).
# Alice likes her candies very much,
# and she wants to eat the maximum number of different types of candies
# while still following the doctor's advice.
#
# Given the integer array candyType of length n,
# return the maximum number of different types of candies
# she can eat if she only eats n / 2 of them.

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        # type_n, can_eat = len(set(candyType)), len(candyType) // 2
        #
        # return min(type_n, can_eat)

        # with Brute Force Algorithm
        # unique_candies = 0
        # for i in range(len(candyType)):
        #     for j in range(0, i):
        #         if candyType[i] == candyType[j]:
        #             break
        #         else:
        #             unique_candies += 1
        # return min(unique_candies, len(candyType) // 2)

        # with Algorithm - Sorting
        candyType.sort()
        unique_candies = 1
        for i in range(1, len(candyType)):
            if candyType[i] != candyType[i - 1]:
                unique_candies += 1

            if unique_candies == len(candyType) // 2:
                break

        return min(unique_candies, len(candyType) // 2)


obj = Solution()

candyType = [1,1,2,2,3,3]
print(obj.distributeCandies(candyType))     # Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies.
# Since there are only 3 types, she can eat one of each type.

candyType = [1,1,2,3]
print(obj.distributeCandies(candyType))     # Output: 2
# Explanation: Alice can only eat 4 / 2 = 2 candies.
# Whether she eats types [1,2], [1,3], or [2,3],
# she still can only eat 2 different types.

candyType = [6,6,6,6]
print(obj.distributeCandies(candyType))     # Output: 1
# Explanation: Alice can only eat 4 / 2 = 2 candies.
# Even though she can eat 2 candies, she only has 1 type.