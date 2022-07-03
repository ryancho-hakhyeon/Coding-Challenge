from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of
# the two subtrees of every node never differs by more than one.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # This is recommended solution.

        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = TreeNode(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root

        return helper(0, len(nums) - 1)


ob = Solution()

nums = [-10, -3, 0, 5, 9]
print(ob.sortedArrayToBST(nums))    # Output: [0,-3,9,-10,null,5]
# [0,-10,5,null,-3,null,9] is also accepted:

nums = [1, 3]
print(ob.sortedArrayToBST(nums))    # Output: [3,1]
# [1,null,3] and [3,1] are both height-balanced BSTs.