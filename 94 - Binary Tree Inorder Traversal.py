from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return the inorder traversal of its nodes' values.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # res = []
        # if root:
        #     res = self.inorderTraversal(root.left)
        #     res.append(root.val)
        #     res = res + self.inorderTraversal(root.right)
        # else:
        #     return res
        # return res

        if root == None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


ob = Solution()

root = [1, None, 2, 3]
print(ob.inorderTraversal(root))  # Output: [1,3,2]

root = [1]
print(ob.inorderTraversal(root))  # Output: [1]

root = []
print(ob.inorderTraversal(root))  # Output: []
