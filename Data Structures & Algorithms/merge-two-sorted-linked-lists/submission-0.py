# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currList1, currList2 = list1, list2
        mergedList = ListNode()
        headMergedList = mergedList

        while currList1 and currList2:
            if currList1.val < currList2.val:
                mergedList.next = currList1
                mergedList = mergedList.next
                currList1 = currList1.next
            else:
                mergedList.next = currList2
                mergedList = mergedList.next
                currList2 = currList2.next
        if not currList1:
            mergedList.next = currList2
        if not currList2:
            mergedList.next = currList1

        return headMergedList.next