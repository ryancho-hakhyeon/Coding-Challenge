from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following definition:
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        cur, nxt = root, root.left if root else None

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur:
                cur = nxt
                nxt = cur.left
        return root


ob = Solution()

root = [1, 2, 3, 4, 5, 6, 7]
print(ob.connect(root))     # Output: [1,#,2,3,#,4,5,6,7,#]
# Given the above perfect binary tree (Figure A),
# your function should populate each next pointer to point to its next right node,
# just like in Figure B.
# The serialized output is in level order as connected by the next pointers,
# with '#' signifying the end of each level.

root = [
print(ob.connect(root))     # Output: []