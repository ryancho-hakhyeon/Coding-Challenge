# The next greater element of some element x in an array
# is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2,
# where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that
# nums1[i] == nums2[j] and determine the next greater element
# of nums2[j] in nums2.
# If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that
# ans[i] is the next greater element as described above.
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        res = []
        stack = []

        for n2 in nums2:
            while stack and n2 > stack[-1]:
                ans[stack.pop()] = n2
            stack.append(n2)

        for n1 in nums1:
            res.append(ans.get(n1, -1))

        return res
        # Hash Map Solution
        # d = defaultdict(lambda: 0)
        # for i in range(len(nums1)):
        #     d[nums1[i]] = i
        # st, ans = [], [0] * len(nums1)
        # j = len(nums2) - 1
        # while j >= 0:
        #     if nums2[j] in d:
        #         if st == []:
        #             ans[d[nums2[j]]] = -1
        #         elif st != [] and st[-1] > nums2[j]:
        #             ans[d[nums2[j]]] = st[-1]
        #         elif st != [] and st[-1] <= nums2[j]:
        #             while st != [] and st[-1] <= nums2[j]:
        #                 st.pop()
        #             if st == []:
        #                 ans[d[nums2[j]]] = -1
        #             else:
        #                 ans[d[nums2[j]]] = st[-1]
        #     st.append(nums2[j])
        #     j -= 1
        # return ans


obj = Solution()

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(obj.nextGreaterElement(nums1, nums2))     # Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element,
# so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element,
# so the answer is -1.

nums1 = [2,4]
nums2 = [1,2,3,4]
print(obj.nextGreaterElement(nums1, nums2))     # Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element,
# so the answer is -1.