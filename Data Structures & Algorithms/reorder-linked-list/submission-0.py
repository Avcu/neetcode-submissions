# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is in the middle, now reverse the second half
        curr = slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
        
        # now prev has the second list but reversed
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            first.next.next = temp1
            first, second = temp1, temp2
        

