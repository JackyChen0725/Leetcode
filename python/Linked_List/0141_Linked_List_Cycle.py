"""
Link: https://leetcode.com/problems/linked-list-cycle/

Solution1: Floyd's Tortoise and Hare algorithm.
    Time Complexity: O(n).
    Space Complexity: O(1).

Solution2: Use Set to store visited nodes.
    Time Complexity: O(n).
    Space Complexity: O(n).
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
        return False

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        cur = head
        
        while cur:
            if cur in nodeSet:
                return True
            nodeSet.add(cur)
            cur = cur.next
        return False