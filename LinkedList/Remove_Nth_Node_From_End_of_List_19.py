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
        # # reverse list
        # cur = head
        # prev = None
        
        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp
        
        # reverse = prev

        # if n ==1 or not reverse:
        #     return reverse.next
        
        # # find and remove node
        # cur = reverse
        # count = 1
        # prev = ListNode(0, reverse)

        # while n != count: # Finding the node
        #     prev = cur
        #     cur = cur.next
        #     count += 1 

        # temp = cur.next # Removing the node
        # cur.next = None
        # prev.next = temp

        # # reverse list again
        # prev = None
        # while reverse:
        #     temp = reverse.next
        #     reverse.next = prev
        #     prev = reverse
        #     reverse = temp
        
        # head = prev
        # return head

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
    
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     dummy = ListNode(0, head)
    #     left = dummy
    #     right = head

    #     while n > 0:
    #         right = right.next
    #         n -= 1

    #     while right:
    #         left = left.next
    #         right = right.next

    #     # delete
    #     left.next = left.next.next
    #     return dummy.next