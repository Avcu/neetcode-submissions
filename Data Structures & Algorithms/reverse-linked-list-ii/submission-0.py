# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        l, r = dummy, dummy

        for idx in range(left-1):
            l = l.next
        for idx in range(right):
            r = r.next

        tail = l
        after = r.next
        prev, curr = None, l.next
        while curr != after:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        tail.next.next = curr
        tail.next = prev
        return dummy.next