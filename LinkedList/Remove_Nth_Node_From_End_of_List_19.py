# Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length
        cur = head
        lenght = 0
        
        while cur:
            cur = cur.next
            lenght += 1

        # get the difference bettween the length and n
        idx = lenght - n
        
        if idx < 0:
            return head

        # Traverese and remove node
        cur = head
        prev = head
        
        if idx == 0:
            return head.next

        while idx > 0:
            prev = cur
            cur = cur.next
            idx -= 1
        
        temp = cur.next
        cur.next = None
        prev.next = temp

        return head
