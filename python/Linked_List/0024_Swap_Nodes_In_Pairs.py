"""
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Solution: Iterative approach.
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        
        cur = dummyHead
        while cur.next and cur.next.next:
            tmp = cur.next.next.next
            cur.next.next.next = cur.next
            cur.next = cur.next.next
            cur.next.next.next = tmp
            cur = cur.next.next
        return dummyHead.next