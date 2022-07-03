from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, level, res):
            if not node:
                return

            if len(res) <= level:
                res += [[]]
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)

            res[level].append(node.val)

        dfs(root, 0, res)

        return len(res)


ob = Solution()

root = [3, 9, 20, None, None, 15, 7]
print(ob.maxDepth(root))    # Output: 3

root = [1, None, 2]
print(ob.maxDepth(root))    # Output: 2
