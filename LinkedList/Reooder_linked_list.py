# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.


# Example1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Example2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]

# [1,2,3,4,5]
# [1,5,3,4,2]
# [1,5,2,4,3]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle -> to beak the list in two
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        second_list = temp

        # Reverse half of the list
        prev = None
        while second_list:
            temp = second_list.next
            second_list.next = prev
            prev = second_list
            second_list = temp

        # Merge List
        second_list = prev
        cur = head
        

        while second_list:
            temp1 = cur.next
            sec1 = second_list.next

            cur.next = second_list
            second_list.next = temp1

            cur = temp1
            second_list = sec1
