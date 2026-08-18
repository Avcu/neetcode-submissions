# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kthNode = head

        idx = 0
        while idx < k and kthNode:
            kthNode = kthNode.next
            idx += 1
        
        if idx == k:
            kthNode = self.reverseKGroup(kthNode, k)
            
            while idx > 0:
                temp = head.next
                head.next = kthNode

                kthNode = head
                head = temp
                idx -= 1

            head = kthNode
        return head
        


            
