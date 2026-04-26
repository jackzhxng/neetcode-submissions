# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time taken: 4 min
        """
        curr1, curr2 = list1, list2
        res = ListNode(-1) # Dummy node
        curr_res = res
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr_res.next = curr1
                curr1 = curr1.next
            else:
                curr_res.next = curr2
                curr2 = curr2.next
            curr_res = curr_res.next
        while curr1:
            curr_res.next = curr1
            curr1 = curr1.next
            curr_res = curr_res.next
        while curr2:
            curr_res.next = curr2
            curr2 = curr2.next
            curr_res = curr_res.next
        return res.next