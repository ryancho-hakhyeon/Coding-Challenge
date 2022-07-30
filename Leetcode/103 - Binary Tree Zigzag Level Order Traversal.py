from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values.
# (i.e., from left to right, then right to left for the next level and alternate between).
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # This is a solution from 102 with few lines adding
        # res = []
        #
        # q = deque()
        # q.append(root)
        # left = False
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
        #         if left:
        #             res.append(level[::-1])
        #         else:
        #             res.append(level)
        #     left = not left
        #
        # return res


        res = []

        def dfs(node, level, res):
            if not node:
                return

            if len(res) <= level:
                res += [[]]

            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)

            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)

        dfs(root, 0, res)

        return res




ob = Solution()

root = [3, 9, 20, None, None, 15, 7]
print(ob.zigzagLevelOrder(root))  # Output: [[3],[20,9],[15,7]]

root = [1]
print(ob.zigzagLevelOrder(root))  # Output: [[1]]

root = []
print(ob.zigzagLevelOrder(root))  # Output: []