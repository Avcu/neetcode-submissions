# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        valHeap = []
        resList = ListNode()
        ite = resList

        for idx in range(len(lists)):
            if lists[idx]:
                heappush(valHeap, [lists[idx].val, idx])
                lists[idx] = lists[idx].next
        
        while valHeap:
            poppedVal, poppedIdx = heappop(valHeap)
            newNode = ListNode(val=poppedVal)
            ite.next = newNode
            ite = ite.next

            if lists[poppedIdx]:
                heappush(valHeap, [lists[poppedIdx].val, poppedIdx])
                lists[poppedIdx] = lists[poppedIdx].next
        
        return resList.next
                