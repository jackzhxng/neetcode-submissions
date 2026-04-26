# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time taken: 5 mins

        Bit rusty
        """
        if not head or not head.next:
            return head
        prev = head
        curr = head.next
        prev.next = None
        while curr:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        return prev
