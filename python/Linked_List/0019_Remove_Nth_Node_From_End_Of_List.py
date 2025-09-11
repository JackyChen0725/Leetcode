"""
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Solution: Slow and fast pointers.
    Time Complexity: O(n).
    Space Complexity: O(1).
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        slow = fast = dummyHead

        for _ in range(n + 1):
            fast = fast.next
            
        while fast != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummyHead.next