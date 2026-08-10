# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2
        resultHead = ListNode(val=0)
        currResult = resultHead

        while curr1 or curr2 or carry != 0:
            currDigit = carry
            if curr1:
                currDigit += curr1.val
                curr1 = curr1.next
            if curr2:
                currDigit += curr2.val
                curr2 = curr2.next

            if currDigit < 10:
                newNode = ListNode(val=currDigit)
                currResult.next = newNode
                currResult = currResult.next
                carry = 0
            else:
                newNode = ListNode(val=currDigit-10)
                currResult.next = newNode
                currResult = currResult.next
                carry = 1
        return resultHead.next