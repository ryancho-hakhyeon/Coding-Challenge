from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.ismirror(root.left, root.right)

    def ismirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.ismirror(leftroot.right, rightroot.left) \
                   and self.ismirror(leftroot.left, rightroot.right)
        return leftroot == rightroot


ob = Solution()

root = [1,2,2,3,4,4,3]
print(ob.isSymmetric(root)) # Output: true

root = [1,2,2,None,3,None,3]
print(ob.isSymmetric(root)) # Output: false