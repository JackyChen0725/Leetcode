"""
Link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Solution1: Swap values.
    Time Complexity: O(n).
    Space Complexity: O(1).

Solution2: Swap nodes.
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        slow = fast = dummyHead
        
        for _ in range(k):
            fast = fast.next
        first = fast
        
        while fast != None:
            slow = slow.next
            fast = fast.next
        second = slow

        first.val, second.val = second.val, first.val
        
        return dummyHead.next

class Solution2:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(next=head)
        pre_left = pre_right = dummyHead
        left = right = dummyHead.next
        
        for _ in range(k - 1):
            pre_left = left
            left = left.next
        
        tmp = left
        while tmp.next != None:
            pre_right = right
            right = right.next
            tmp = tmp.next
        
        if left == right:
            return dummyHead.next

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next
        return dummyHead.next