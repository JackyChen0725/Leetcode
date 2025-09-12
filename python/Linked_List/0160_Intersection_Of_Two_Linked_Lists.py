"""
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Solution: Traverse + Reverse + Traverse again.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Traverse list B and store node values in an array
        arr = []
        
        cur = headB
        while cur:
            arr.append(cur.val)
            cur = cur.next

        # Reverse list A
        cur = headA
        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        # Traverse list B again and identify the different position
        cur = headB
        idx = 0
        while cur.next:
            if cur.next.val != arr[idx + 1]:
                return cur
            cur = cur.next
            idx += 1
        return None