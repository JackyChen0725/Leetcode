"""
Link: https://leetcode.com/problems/linked-list-cycle-ii/

Solution: Floyd's Tortoise and Hare algorithm.
    1. Use two pointers (slow and fast) to detect a cycle.
    2. If a cycle is detected, find the entry point of the cycle.
    Time Complexity: O(n).
    Space Complexity: O(1).
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            return None

        tmp1 = head
        tmp2 = fast
        while tmp1 != tmp2:
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        
        return tmp1