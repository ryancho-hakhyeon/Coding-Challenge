# You are given an integer array score of size n,
# where score[i] is the score of the ith athlete in a competition.
# All the scores are guaranteed to be unique.
#
# The athletes are placed based on their scores,
# where the 1st place athlete has the highest score,
# the 2nd place athlete has the 2nd highest score, and so on.
# The placement of each athlete determines their rank:
#
# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete,
# their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = []
        sorted_score = sorted(score)[::-1]
        # print(score)
        # print(sorted_score)

        for i in range(len(score)):
            if score[i] == sorted_score[0]:
                ans.append('Gold Medal')
            elif score[i] == sorted_score[1]:
                ans.append('Silver Medal')
            elif score[i] == sorted_score[2]:
                ans.append('Bronze Medal')
            else:
                ans.append(str(sorted_score.index(score[i]) + 1))

        return ans


obj = Solution()

score = [5,4,3,2,1]
print(obj.findRelativeRanks(score))
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
# Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

score = [10,3,8,9,4]
print(obj.findRelativeRanks(score))
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
# Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
