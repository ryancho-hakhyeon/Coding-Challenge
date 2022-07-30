from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return the level order traversal of its nodes' values.
# (i.e., from left to right, level by level).
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This is solution from discussion
        # res = []
        #
        # q = deque()
        # q.append(root)
        #
        # while q:
        #     qLen = len(q)
        #     level = []
        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             level.append(node.val)
        #             q.append(node.left)
        #             q.append(node.right)
        #     if level:
        #         res.append(level)
        # return res

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

        return res


ob = Solution()

root = [3, 9, 20, None, None, 15, 7]
print(ob.levelOrder(root))  # Output: [[3],[9,20],[15,7]]

root = [1]
print(ob.levelOrder(root))  # Output: [[1]]

root = []
print(ob.levelOrder(root))  # Output: []