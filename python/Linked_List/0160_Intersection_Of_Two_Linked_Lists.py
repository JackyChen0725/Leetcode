"""
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

Solution1:
    1. Compute the lengths of both linked lists.
    2. Align the start pointers of both lists.
    3. Traverse both lists simultaneously to find the intersection node.
    Time Complexity: O(m + n), where m and n are the lengths of the two linked lists.
    Space Complexity: O(1).

Solution2:
    1. Use two pointers to traverse both lists.
    2. When a pointer reaches the end of a list, redirect it to the head of the other list.
    3. If the lists intersect, the pointers will meet at the intersection node after at most two passes.
    Time Complexity: O(m + n), where m and n are the lengths of the two linked lists.
    Space Complexity: O(1).
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Traverse list A and B to get their lengths
        curA, curB = headA, headB
        lenA = lenB = 0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next

        # Align the start pointers of both lists
        if lenA >= lenB:
            curLong = headA
            curShort = headB
        else:
            curLong = headB
            curShort = headA
        
        for _ in range(abs(lenA - lenB)):
            curLong = curLong.next
        
        # Traverse both lists to find the intersection
        while curLong and curShort:
            if curLong == curShort:
                return curLong
            curLong = curLong.next
            curShort = curShort.next
        return None

class Soltuion2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA, curB = headA, headB
        
        while curA != curB:
            curA = curA.next
            curB = curB.next
            
            if curA == curB:
                return curA

            if curA == None:
                curA = headB
            if curB == None:
                curB = headA
        return curA