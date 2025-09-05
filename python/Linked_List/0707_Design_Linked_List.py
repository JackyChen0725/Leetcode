"""
Link: https://leetcode.com/problems/design-linked-list/

Solution: Singly linked list.
    Time Complexity: O(n) for get, addAtTail, addAtIndex, deleteAtIndex; O(1) for addAtHead.
    Space Complexity: O(n).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.dummy_head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val=val)
        node.next = self.dummy_head.next
        self.dummy_head.next = node
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        node = ListNode(val=val)
        cur = self.dummy_head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        node = ListNode(val=val)
        cur = self.dummy_head
        while index:
            cur = cur.next
            index -= 1
        node.next = cur.next
        cur.next = node
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        cur = self.dummy_head
        while index:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1
        return

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)