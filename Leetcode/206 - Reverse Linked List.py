# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            ntx = curr.next
            curr.next = prev
            prev = curr
            curr = ntx

        return prev


ob = Solution()

head = [1,2,3,4,5]
ob.reverseList(head)    # Output : [5,4,3,2,1]

head = [1,2]
ob.reverseList(head)    # Output : [2,1]
