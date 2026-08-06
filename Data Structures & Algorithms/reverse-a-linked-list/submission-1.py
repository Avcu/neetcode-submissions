# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # prev -> curr -> temp
            temp = curr.next

            # prev <- curr || temp 
            curr.next = prev

            prev = curr
            curr = temp
        return prev