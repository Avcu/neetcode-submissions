# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        while head is not None:
            head.val = float('inf')

            if head.next is not None and head.next.val == float('inf'):
                return True
            else:
                head = head.next
        return False
        