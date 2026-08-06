# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeCount = 0
        curr = head
        while curr:
            nodeCount += 1
            curr = curr.next

        removeIdx = nodeCount - n
        curr = head
        if removeIdx == 0:
            return head.next
        else:
            for i in range(removeIdx-1):
                curr = curr.next
            curr.next = curr.next.next
            return head