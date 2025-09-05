"""
Link: https://leetcode.com/problems/remove-linked-list-elements/

Solution: Use a dummy head to simplify edge cases.
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


if __name__ == "__main__":
    solution = Solution()
    # head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    # val = 6
    
    # head = None
    # val = 1
    
    head = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
    val = 7
    result = solution.removeElements(head, val)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")