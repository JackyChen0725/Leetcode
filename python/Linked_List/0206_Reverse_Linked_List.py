"""
Link: https://leetcode.com/problems/reverse-linked-list/

Solution1: Three pointers.
    Time Complexity: O(n).
    Space Complexity: O(1).

Solution2: Recursion.
    Time Complexity: O(n).
    Space Complexity: O(n).
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, cur):
            if cur is None:
                return prev
            
            tmp = cur.next
            cur.next = prev
            return reverse(cur, tmp)
        return reverse(None, head)